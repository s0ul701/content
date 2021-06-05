from django.db import models


class ViewCountMixin(models.Model):
    view_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
    )

    class Meta:
        abstract = True
