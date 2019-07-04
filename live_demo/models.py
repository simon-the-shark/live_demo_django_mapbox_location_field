from django.db import models
from mapbox_location_field.models import LocationField


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72"})
