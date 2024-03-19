# Generated by Django 5.0.3 on 2024-03-19 00:02

import mapbox_location_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': (17.031645, 51.106715), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'})),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', mapbox_location_field.models.AddressAutoHiddenField(map_id='map')),
            ],
        ),
    ]
