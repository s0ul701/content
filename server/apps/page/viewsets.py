from rest_framework import mixins, pagination, response, viewsets

from .models import Page
from .serializers import PageListSerializer, PageRetrieveSerializer


class PagePagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return response.Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data,
        })


class PageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    pagination_class = PagePagination
    serializers_by_actions_mapping = {
        'list': PageListSerializer,
        'retrieve': PageRetrieveSerializer,
    }
    queryset_by_actions_mapping = {
        'list': Page.objects.values_list('id', flat=True),
        'retrieve': Page.objects.with_prefetched_contents(),
    }

    def get_queryset(self):
        return self.queryset_by_actions_mapping[self.action]

    def get_serializer_class(self):
        return self.serializers_by_actions_mapping[self.action]
