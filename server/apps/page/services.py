from typing import NoReturn

from django.db import models, transaction


def _increment_contents_view_count(page) -> NoReturn:
    @transaction.atomic
    def increment_content_view_count() -> NoReturn:
        content.all().select_for_update().update(
            view_count=models.F('view_count') + 1,
        )

    contents_names_for_increment_view_count = ('audios', 'texts', 'videos')
    for content_name in contents_names_for_increment_view_count:
        content = getattr(page, content_name)
        increment_content_view_count()
