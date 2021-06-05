from django.db import models

from apps.core.models.mixins import ViewCountMixin


class Page(ViewCountMixin):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'
