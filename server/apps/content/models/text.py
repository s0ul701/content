from django.db import models
from django.utils.text import Truncator

from .mixins import ViewCountMixin


class Text(ViewCountMixin):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pages = models.ManyToManyField(
        to='page.Page',
        through='content.PageTexts',
        related_name='texts',
        verbose_name='Страницы',
    )

    def __str__(self):
        return f'{self.title} ({Truncator(self.text).chars(50, "...")})'

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class PageTexts(models.Model):
    page = models.ForeignKey(
        to='page.Page',
        on_delete=models.CASCADE,
    )
    text = models.ForeignKey(
        to='content.Text',
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Text #{self.order}'

    class Meta:
        ordering = ('order',)
        verbose_name = 'Текст на Страницу'
        verbose_name_plural = 'Тексты на Странице'
