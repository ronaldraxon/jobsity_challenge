"""
data_extraction_manager.views.serializers.FileSerializer.py
===========================================================

"""
from rest_framework import serializers
from data_extraction_manager.models.File import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
