from django.forms import ModelForm
from data_extraction_manager.models.File import File


class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = "__all__"
