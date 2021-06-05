from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

from .models import Page


class AudioInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Page.audios.through
    extra = 0


class TextInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Page.texts.through
    extra = 0


class VideoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Page.videos.through
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (AudioInline, TextInline, VideoInline)
    readonly_fields = ('view_count',)
