from django.contrib import admin

from ..models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file', 'subtitles_file')
    readonly_fields = ('view_count',)
