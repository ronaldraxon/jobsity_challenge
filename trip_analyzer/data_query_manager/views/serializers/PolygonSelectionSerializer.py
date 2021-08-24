from rest_framework import serializers
from rest_framework.serializers import ChoiceField
from django.utils.safestring import mark_safe
selection_choices = ('Polygon', 'Polygon')


class PolygonSelectionSerializer(serializers.Serializer):
    type = ChoiceField(choices=selection_choices,
                       allow_blank=False,
                       help_text=mark_safe("<strong>Shape Selection Type.</strong>"))
    coordinates = serializers.ListField(allow_empty=False,
                                        child= serializers.ListField(allow_empty=False,
                                                                     child= serializers.ListField(allow_empty=False,
                                                                                                  child=serializers.FloatField())),
                                        help_text=mark_safe("<strong>List of input variables.</strong>"))
