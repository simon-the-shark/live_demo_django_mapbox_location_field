from django.views.generic import CreateView, UpdateView

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
