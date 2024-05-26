# Create your views here.
from django.views.generic import ListView

from esystem.models import HazardousWasteSystem


class HazardousWasteSystemListView(ListView):
    model = HazardousWasteSystem
    template_name = "esystem/hazardouswastesystem_list.html"
    context_object_name = "hazardouswastesystems"
    paginate_by = 10
