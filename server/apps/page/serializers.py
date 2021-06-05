from rest_framework import reverse, serializers

from apps.content.serializers import (
    AudioSerializer, TextSerializer, VideoSerializer,
)
from .models import Page


class PageListSerializer(serializers.Serializer):
    def to_representation(self, page_id: int) -> str:
        view_name = (
            f'{self.context["request"]._request.resolver_match.namespace}:'
            f'{self.context["view"].basename}-detail'
        )
        return reverse.reverse(
            view_name,
            args=(page_id,),
            request=self.context['request'],
        )


class PageRetrieveSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True)
    texts = TextSerializer(many=True)
    videos = VideoSerializer(many=True)

    class Meta:
        model = Page
        fields = ('title', 'view_count', 'audios', 'texts', 'videos')
