"""
trip_business.models.Region.py
==============================
Dimension table for Trip (Fact Table)
"""

from django.utils.safestring import mark_safe
from django.contrib.gis.db import models
from uuid import uuid4


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, default="Unknown",
                                   help_text=mark_safe("<strong>Region's canonical name .</strong>"))

    def __str__(self):
        return self.name

    class Meta:
         """Associated table in db.
         """
         db_table = "region"