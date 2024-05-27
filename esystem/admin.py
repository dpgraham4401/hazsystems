# Register your models here.
from django.contrib import admin
from django.contrib.admin import register

from esystem.models import HazardousWasteSystem


@register(HazardousWasteSystem)
class HazardousWasteSystemAdmin(admin.ModelAdmin):
    pass
