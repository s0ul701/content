from django.db import models

from .managers import PageManager


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    objects = PageManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'
