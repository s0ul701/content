from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.page.viewsets import PageViewSet

app_name = 'api'

router = SimpleRouter()
router.register('pages', PageViewSet, basename='pages')

urlpatterns = [path('', include(router.urls))]
