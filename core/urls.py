from django.urls import path
from django.urls.conf import include

from core.views import home_view

urlpatterns = [
    path("", include([
        path("", home_view, name="home"),
    ]))
]
