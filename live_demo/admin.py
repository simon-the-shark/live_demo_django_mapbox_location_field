from django.contrib import admin
from mapbox_location_field.admin import MapAdmin
from .models import Place

admin.site.register(Place, MapAdmin)
# Register your models here.
