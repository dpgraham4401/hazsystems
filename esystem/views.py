# Create your views here.
from django.views.generic import CreateView, DetailView, ListView

from esystem.forms import HazardousWasteSystemForm
from esystem.models import HazardousWasteSystem


class HazardousWasteSystemListView(ListView):
    model = HazardousWasteSystem
    template_name = "esystem/hazardouswastesystem_list.html"
    context_object_name = "hazardouswastesystems"
    paginate_by = 10


class HazardousWasteSystemDetailView(DetailView):
    model = HazardousWasteSystem
    template_name = "esystem/hazardouswastesystem_detail.html"


class HazardousWasteSystemCreateView(CreateView):
    form_class = HazardousWasteSystemForm
    template_name = "esystem/hazardouswastesystem_form.html"
    success_url = "/system/"
