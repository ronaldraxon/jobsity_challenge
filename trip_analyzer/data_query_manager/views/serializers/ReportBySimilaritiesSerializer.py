from rest_framework import serializers
from django.utils.safestring import mark_safe

class ReportBySimilaritiesSerializer(serializers.Serializer):
    origin = serializers.FloatField(help_text=mark_safe("<strong>Selection Type.</strong>"))
    destination = serializers.FloatField(help_text=mark_safe("<strong>Selection Type.</strong>"))
    hour_of_day = serializers.IntegerField(help_text=mark_safe("<strong>Selection Type.</strong>"))
    count = serializers.IntegerField(help_text=mark_safe("<strong>Selection Type.</strong>"))




