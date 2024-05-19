from django.urls import path

from esystem.views import HazardousWasteSystemListView

urlpatterns = [
    path("", HazardousWasteSystemListView.as_view()),
]
