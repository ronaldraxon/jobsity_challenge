"""
data_extraction_manager.views.urls.py
===============================

"""

from django.urls import path
from data_extraction_manager.views.FileUploadView import FileUploadView

app_name = "data_extraction_manager"
urlpatterns = [
    path('fileupload', FileUploadView.as_view(), name="csv_file_upload")
]