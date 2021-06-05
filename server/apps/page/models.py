from typing import NoReturn

from django.db import models

from .managers import PageManager
from .services import _increment_contents_view_count


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    objects = PageManager()

    def increment_contents_view_count(self) -> NoReturn:
        _increment_contents_view_count(self)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'
