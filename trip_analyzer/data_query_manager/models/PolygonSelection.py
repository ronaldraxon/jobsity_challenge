"""
data_registry.models.DataAsset.py
=================================
Modulo de definición del activo de datos destinado a una tarea de minería.
"""

from django.contrib.gis.db import models
from django.utils.safestring import mark_safe

class PolygonSelection(models.Model):

    selection = models.PolygonField(help_text=mark_safe("<strong>Defined Polygon to create a selection "
                                                        "Example: POLYGON( ((0.0 0.0), (0.0 50.0), (50.0 50.0), "
                                                        "(50.0 0.0), (0.0 0.0)) ).</strong>"))

    class Meta:
        managed = False