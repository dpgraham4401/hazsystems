from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

from waste.views import WasteListView

app_name = "waste"
urlpatterns = [
    path("waste", WasteListView.as_view(), name="waste-list"),
]
