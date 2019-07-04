from django.urls import re_path

from .views import AddPlaceView, ChangePlaceView

urlpatterns = [
    re_path("^$", AddPlaceView.as_view(), name="add"),
    re_path("^places/(?P<pk>[0-9]+)/$", ChangePlaceView.as_view(), name="change"),

]
