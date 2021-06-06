import re
from typing import Dict, NoReturn, Union

from django.db import models, transaction
from django.forms.models import BaseInlineFormSet
from rest_framework import reverse, serializers

from apps.content.models import Audio, Text, Video
from apps.content.serializers import (
    AudioSerializer, TextSerializer, VideoSerializer,
)

CONTENT_NAMES = ('audios', 'texts', 'videos')
CONTENT_MODELS = (Audio, Text, Video)
CONTENT_SERIALIZERS = (AudioSerializer, TextSerializer, VideoSerializer)


class PageTasksService:
    """Сервис, отвечающий Celery-таски в контексте сущности Страницы"""
    @staticmethod
    def increment_contents_view_count(page) -> NoReturn:
        """
        Атомарно увеличивает количество просмотров каждого
        объекта Контента
        """
        @transaction.atomic
        def increment_content_view_count() -> NoReturn:
            content.all().select_for_update().update(
                view_count=models.F('view_count') + 1,
            )

        for content_name in CONTENT_NAMES:
            content = getattr(page, content_name)
            increment_content_view_count()


class PageAdminValidationService:
    """
    Сервис, отвечающий за валидацию Страницы,
    при взаимодействии с ней через админку
    """
    @staticmethod
    def validate_contents_orders(
        content_formset: BaseInlineFormSet,
    ) -> NoReturn:
        """
        Валидирует значения порядков отображения разных типов
        контента совметсно
        """
        current_content_fields_pattern = re.compile(
            r'{prefix}-\d+-order'.format(prefix=content_formset.prefix),
        )
        current_content_order_fields = tuple(
            field for field in content_formset.data.keys()
            if current_content_fields_pattern.match(field)
        )
        current_orders = tuple(
            content_formset.data[field]
            for field in current_content_order_fields
        )
        if len(current_orders) != len(set(current_orders)):
            content_formset._non_form_errors.append(
                'Порядок некоторых элементов внутри блока совпадает!',
            )

        order_fields_pattern = re.compile(r'^.+set-\d+-order$')
        other_order_fields = tuple(
            field for field in content_formset.data.keys()
            if order_fields_pattern.match(field)
            and field not in current_content_order_fields
        )
        other_orders = tuple(
            content_formset.data[field] for field in other_order_fields
        )
        if set.intersection(set(current_orders), set(other_orders)):
            content_formset._non_form_errors.append(
                'Порядок некоторых элементов данного блока совпадает '
                'с порядком элементов в других блоках контента совпадает!',
            )


class PageManagerService:
    """Сервис, реализующий функционал ModelManager'а для Страницы"""
    def get_prefetched_annotated_content(
        page_manager: models.Manager,
    ) -> models.query.QuerySet:
        """
        Возвращает QuerySet Страниц с предзагруженным контентом,
        каждый объект которого проанотирован порядком отображения
        """
        return page_manager.prefetch_related(
            *[
                models.Prefetch(
                    content_name,
                    queryset=content_model.objects.order_by(
                        f'page{content_name}__order'
                    ).annotate(
                        order=models.query.F(f'page{content_name}__order')
                    ),
                )
                for content_name, content_model in zip(
                    CONTENT_NAMES, CONTENT_MODELS,
                )
            ]
        )


class PageSerializersService:
    """Сервис, отвечающий за логику сериалайзеров для Страницы"""
    @staticmethod
    def get_page_url(serializer: serializers.Serializer, page_id: int) -> str:
        """
        Возвращает полный URL для получения детальной информации
        по Странице
        """
        view_name = (
            f'{serializer.context["request"]._request.resolver_match.namespace}:'
            f'{serializer.context["view"].basename}-detail'
        )
        return reverse.reverse(
            view_name,
            args=(page_id,),
            request=serializer.context['request'],
        )

    @staticmethod
    def _get_serialized_content_item(
        content_item: Union[CONTENT_MODELS],
    ) -> Dict:
        """
        На основе полученного объекта контента определяет подходящий
        сериалайзер и возвращает его сериализованное представление
        """
        serializer = tuple(filter(
            lambda serializer_class:
                content_item.__class__ == serializer_class.Meta.model,
            CONTENT_SERIALIZERS
        ))[0]
        return serializer(content_item).data

    @classmethod
    def get_formed_content(cls, page) -> Dict:
        """Возвращает сериализованный контент"""
        content = []
        for content_name in CONTENT_NAMES:
            content.extend(getattr(page, content_name).all())
        content.sort(key=lambda content_item: content_item.order)

        return [
            cls._get_serialized_content_item(content_item)
            for content_item in content
        ]
