from django.views.generic import CreateView, UpdateView, ListView

from .models import Place


class AddPlaceView(CreateView):
    model = Place
    template_name = "live_demo/place_form.html"
    success_url = "/index/"
    fields = ("location", "address")


class ChangePlaceView(UpdateView):
    model = Place
    template_name = "live_demo/place_form.html"
    success_url = "/index/"
    fields = ("location", "address")


class PlacesView(ListView):
    model = Place
    template_name = "live_demo/index.html"
    ordering = ["-created_at", ]
