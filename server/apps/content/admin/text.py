from django.contrib import admin

from ..models import Text


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('view_count',)
