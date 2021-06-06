from rest_framework import serializers

from .models import Page
from .services import PageSerializersService


class PageListSerializer(serializers.Serializer):
    def to_representation(self, page_id: int) -> str:
        return PageSerializersService.get_page_url(self, page_id)


class PageRetrieveSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, page: Page):
        return PageSerializersService.get_formed_content(page)

    class Meta:
        model = Page
        fields = ('title', 'content')
