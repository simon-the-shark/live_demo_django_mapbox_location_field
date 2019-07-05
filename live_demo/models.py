from django.db import models
from mapbox_location_field.models import LocationField


class Place(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72"})
    created_at = models.DateTimeField(auto_now_add=True)
