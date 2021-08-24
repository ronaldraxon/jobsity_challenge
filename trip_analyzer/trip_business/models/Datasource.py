"""
trip_business.models.Datasource.py
==================================
Dimension table for Trip
"""

from django.utils.safestring import mark_safe
from django.contrib.gis.db import models
from trip_business.models.Region import Region
from django.utils import timezone
from uuid import uuid4


class Datasource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, default="Unknown",
                                       help_text=mark_safe("<strong>Datasource's canonical name.</strong>"))

    def __str__(self):
        return self.name

    class Meta:
        """Associated table in db.
        """
        db_table = "datasource"