"""
c4ufb.business.views.BusinessUnitView.py
===============================
Modulo para la visualizacion de los metodos del ATM.
"""
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import BaseParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.views.generic.edit import FormView
from data_extraction_manager.forms.FileUploadForm import FileUploadForm
from data_extraction_manager.services.FileUploadService import FileUploadService
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics


class FileUploaderView(FormView):
    form_class = FileUploadForm
    template_name = 'FileUpload.html'  # Replace with your template.

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            file_path =FileUploadService.handle_uploaded_file(request.FILES['file'])
            FileUploadService.load_data_from_file(file_path)
            return HttpResponse('The file was saved')
        else:
            return HttpResponse('The file was not saved')


