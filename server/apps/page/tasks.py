from typing import NoReturn

from config.celery import celery_app

from .models import Page
from .services import PageTasksService


@celery_app.task
def increment_page_contents_view_count_task(page_id: str) -> NoReturn:
    PageTasksService.increment_contents_view_count(Page.objects.get(id=page_id))
