"""
data_extraction_manager.models.File.py
======================================

"""
from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    class Meta:
        managed = False
