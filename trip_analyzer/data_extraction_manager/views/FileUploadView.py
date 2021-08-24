"""
c4ufb.business.views.BusinessUnitView.py
===============================
Modulo para la visualizacion de los metodos del ATM.
"""
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import BaseParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic.edit import FormView

from data_extraction_manager.forms.FileUploadForm import FileUploadForm
from data_extraction_manager.views.Serializers.FileSerializer import FileSerializer

from trip_business.services.RegionService import RegionService
from trip_business.services.DatasourceService import DatasourceService


def handle_uploaded_file(f):
    # with open('some/file/name.txt', 'wb+') as destination:

    all_regions = RegionService.get_all_regions_as_dict()
    all_datasources = DatasourceService.get_all_datasources_as_dict()
    trips = []

    for chunk in f.chunks():
        print(chunk.decode('utf-8'))

# def FileUploadView(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             #form.save()
#             #handle_uploaded_file(request.FILES['file'])
#             return HttpResponse('The file is saved')
#     else:
#         form = FileUploadForm()
#         context = {
#             'form':form,
#         }
#     return render(request, 'FileUpload.html', context)


class FileUploaderView(FormView):
    form_class = FileUploadForm
    template_name = 'FileUpload.html'  # Replace with your template.

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('The file is saved')
        else:
            return HttpResponse('The file is was not saved')
