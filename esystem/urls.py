from django.urls import path
from django.urls.conf import include

from esystem.views import (
    HazardousWasteSystemCreateView,
    HazardousWasteSystemDetailView,
    HazardousWasteSystemListView,
)

urlpatterns = [
    path(
        "system/",
        include(
            [
                path("", HazardousWasteSystemListView.as_view(), name="system_list"),
                path(
                    "create",
                    HazardousWasteSystemCreateView.as_view(),
                    name="system_create",
                ),
                path(
                    "<int:pk>",
                    HazardousWasteSystemDetailView.as_view(),
                    name="system_detail",
                ),
            ]
        ),
    )
]
