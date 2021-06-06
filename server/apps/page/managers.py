from django.db import models

from .services import PageManagerService


class PageManager(models.Manager):
    def with_prefetched_contents(self) -> models.query.QuerySet:
        return PageManagerService.get_prefetched_annotated_content(self)
