from django.urls import path
from django.urls.conf import include

from esystem.views import HazardousWasteSystemListView

urlpatterns = [
    path("system/", include([
        path("", HazardousWasteSystemListView.as_view()),
    ]))
]
