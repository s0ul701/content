from django.contrib import admin

from ..models import Audio


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'bitrate')
    readonly_fields = ('view_count',)
