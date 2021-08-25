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
from django.contrib.gis.geos import GEOSGeometry
from uuid import uuid1


class Trip(models.Model):
    trip_id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, help_text=mark_safe("<strong>Region's uuid.</strong>"))
    _trip_origin_coordinates = models.PointField(help_text=mark_safe("<strong>Tuple representation "
                                                                    "of lat lon of trip origin.</strong>"))
    _trip_destination_coordinates = models.PointField(help_text=mark_safe("<strong>Tuple representation "
                                                                    "of lat lon of trip destination.</strong>"))
    trip_datetime = models.DateTimeField(null=False, default=timezone.now,
                                         help_text=mark_safe("<strong>Date and time when the trip was conducted.</strong>"))
    data_source = models.ForeignKey(Datasource, on_delete=models.PROTECT, help_text=mark_safe("<strong>Datasource's uuid.</strong>"))



    @property
    def trip_origin_coordinates(self):
        return self._trip_origin_coordinates

    @trip_origin_coordinates.setter
    def trip_origin_coordinates(self, point_string):
        self._trip_origin_coordinates = GEOSGeometry(point_string)

    @property
    def trip_destination_coordinates(self):
        return self._trip_destination_coordinates

    @trip_destination_coordinates.setter
    def trip_destination_coordinates(self, point_string):
        self._trip_destination_coordinates = GEOSGeometry(point_string)


    class Meta:
        """Associated table in db.
        """
        db_table = "trip"