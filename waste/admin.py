from django.contrib import admin

from waste.models import Waste, WasteTag


# Register your models here.
@admin.register(Waste)
class WasteAdmin(admin.ModelAdmin):
    pass

@admin.register(WasteTag)
class WasteTagAdmin(admin.ModelAdmin):
    pass
