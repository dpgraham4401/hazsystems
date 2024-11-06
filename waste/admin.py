from django.contrib import admin

from waste.models import Waste


# Register your models here.
@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    pass
