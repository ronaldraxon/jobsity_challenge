from rest_framework import serializers
from django.utils.safestring import mark_safe
from data_query_manager.views.serializers.WeeklyReportLayoutSerializer import WeeklyReportLayoutSerializer


class WeeklyAverageReportSerializer(serializers.Serializer):
    selection_type = serializers.CharField(max_length = 20,
                                           help_text=mark_safe("<strong>Selection Type.</strong>"))
    selector_value = serializers.CharField(max_length = 500,
                                           help_text=mark_safe("<strong>Value assigned by user to conduct the report.</strong>"))
    report = WeeklyReportLayoutSerializer(many=True)
