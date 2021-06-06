from django.forms.models import BaseInlineFormSet

from .services import PageAdminValidationService


class ContentFormSet(BaseInlineFormSet):
    def clean(self):
        PageAdminValidationService.validate_contents_orders(self)
