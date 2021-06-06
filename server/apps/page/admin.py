from django.contrib import admin

from .forms import ContentFormSet
from .models import Page


class AudioInline(admin.TabularInline):
    model = Page.audios.through
    formset = ContentFormSet
    fields = ('order', 'audio')
    extra = 0


class TextInline(admin.TabularInline):
    model = Page.texts.through
    formset = ContentFormSet
    fields = ('order', 'text')
    extra = 0


class VideoInline(admin.TabularInline):
    model = Page.videos.through
    formset = ContentFormSet
    fields = ('order', 'video')
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = (AudioInline, TextInline, VideoInline)
    search_fields = ('title', 'audios__title', 'texts__title', 'videos__title')
