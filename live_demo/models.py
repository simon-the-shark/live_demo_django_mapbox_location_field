from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Place(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", 'center': [0, 100]})
    created_at = models.DateTimeField(auto_now_add=True)
    address = AddressAutoHiddenField()
