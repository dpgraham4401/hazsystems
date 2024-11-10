from django.urls import path

from waste.views import WasteListView

app_name = "waste"
urlpatterns = [
    path("waste", WasteListView.as_view(), name="waste-list"),
]
