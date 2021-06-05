from django.db import models

from apps.content.models import Audio, Text, Video


class PageManager(models.Manager):
    def with_prefetched_contents(self):
        return self.prefetch_related(
            models.Prefetch(
                'audios',
                queryset=Audio.objects.order_by('pageaudios__order'),
            ),
            models.Prefetch(
                'texts',
                queryset=Text.objects.order_by('pagetexts__order'),
            ),
            models.Prefetch(
                'videos',
                queryset=Video.objects.order_by('pagevideos__order'),
            ),
        )
