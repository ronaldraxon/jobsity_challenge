from django.urls import path

from data_extraction_manager.views.FileUploadView import FileCSVView,FileAvroView

app_name = "data_extraction_manager"
urlpatterns = [
    path('csvfileupload', FileCSVView.as_view(), name="csv_file_upload"),
    path('avrofileupload', FileAvroView.as_view(), name="avro_file_upload")
]