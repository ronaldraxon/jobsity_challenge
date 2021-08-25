
from rest_framework import serializers
from django.utils.safestring import mark_safe


class WeeklyReportLayoutSerializer(serializers.Serializer):
    week_number = serializers.IntegerField(help_text=mark_safe("<strong>List of input variables.</strong>"))
    trips_average = serializers.IntegerField(help_text=mark_safe("<strong>Rounded average of trips conducted per day on an specific week.</strong>"))

