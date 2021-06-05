from django.db import models

from apps.core.models.mixins import ViewCountMixin


class Audio(ViewCountMixin):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    bitrate = models.PositiveIntegerField(verbose_name='Битрейт')
    pages = models.ManyToManyField(
        to='page.Page',
        through='content.PageAudios',
        related_name='audios',
        verbose_name='Страницы',
    )

    def __str__(self):
        return f'{self.title} ({self.bitrate} bit/s)'

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'


class PageAudios(models.Model):
    page = models.ForeignKey(
        to='page.Page',
        on_delete=models.CASCADE,
    )
    audio = models.ForeignKey(
        to='content.Audio',
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Audio #{self.order}'

    class Meta:
        ordering = ('order',)
        verbose_name = 'Аудио на Страницу'
        verbose_name_plural = 'Аудио на Странице'
