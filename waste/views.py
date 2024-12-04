from django.shortcuts import render
from django.views.generic import ListView

from waste.models import Waste


# Create your views here.
class WasteListView(ListView):
    """View ALL the waste!"""
    model = Waste
    template_name = "waste/waste_list.html"
    context_object_name = "wastes"
    paginate_by = 30
