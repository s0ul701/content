from rest_framework import serializers

from ..models import Audio


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'title', 'bitrate', 'view_count')
