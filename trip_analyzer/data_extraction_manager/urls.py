from django.urls import path

from data_extraction_manager.views.FileUploadView import FileUploaderView, FileView

app_name = "data_extraction_manager"
urlpatterns = [
    #path('fileuploadr', FileUploaderView.as_view(), name="csv_file_upload"),
    path('fileupload', FileView.as_view(), name="file_upload")
]