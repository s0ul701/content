from django.db import models

from .mixins import ViewCountMixin
from .utils import get_upload_file_path


class Video(ViewCountMixin):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    video_file = models.FileField(
        upload_to=get_upload_file_path,
        verbose_name='Ссылка на Видео',
    )
    subtitles_file = models.FileField(
        upload_to=get_upload_file_path,
        verbose_name='Ссылка на файл Субтитров',
    )
    pages = models.ManyToManyField(
        to='page.Page',
        through='content.PageVideos',
        related_name='videos',
        verbose_name='Страницы',
    )

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class PageVideos(models.Model):
    page = models.ForeignKey(
        to='page.Page',
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        to='content.Video',
        on_delete=models.CASCADE,
    )
    order = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'Video #{self.order}'

    class Meta:
        ordering = ('order',)
        verbose_name = 'Видео на Страницу'
        verbose_name_plural = 'Видео на Странице'
