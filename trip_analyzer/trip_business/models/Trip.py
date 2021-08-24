"""
trip_business.models.Trip.py
============================
Fact table storing trip's data
"""

from django.utils.safestring import mark_safe
from django.contrib.gis.db import models
from trip_business.models.Region import Region
from trip_business.models.Datasource import Datasource
from django.utils import timezone
from uuid import uuid4


class Trip(models.Model):
    trip_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, help_text=mark_safe("<strong>Region's uuid.</strong>"))
    trip_origin_coordinates = models.PointField(help_text=mark_safe("<strong>Tuple representation "
                                                                    "of lat lon of trip origin.</strong>"))
    trip_destination_coordinates = models.PointField(help_text=mark_safe("<strong>Tuple representation "
                                                                    "of lat lon of trip destination.</strong>"))
    trip_datetime = models.DateTimeField(null=False, default=timezone.now,
                                         help_text=mark_safe("<strong>Date and time when the trip was conducted.</strong>"))
    data_source = models.ForeignKey(Datasource, on_delete=models.PROTECT, help_text=mark_safe("<strong>Datasource's uuid.</strong>"))

    def __str__(self):
        return self.name

    class Meta:
        """Associated table in db.
        """
        db_table = "trip"