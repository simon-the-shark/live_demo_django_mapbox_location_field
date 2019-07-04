from django.views.generic import CreateView, UpdateView, ListView

from .models import Place


class AddPlaceView(CreateView):
    model = Place
    template_name = "live_demo/place_form.html"
    success_url = "/index/"
    fields = "__all__"


class ChangePlaceView(UpdateView):
    model = Place
    template_name = "live_demo/place_form.html"
    success_url = "/index/"
    fields = "__all__"

class PlacesView(ListView):
    model = Place
    template_name = "live_demo/index.html"