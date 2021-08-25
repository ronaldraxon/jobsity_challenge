from rest_framework import serializers


# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = "__all__"

class FileSerializer(serializers.Serializer):
    resume = serializers.FileField()
