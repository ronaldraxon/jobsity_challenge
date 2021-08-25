"""
c4ufb.business.views.BusinessUnitView.py
===============================
Modulo para la visualizacion de los metodos del ATM.
"""

from data_extraction_manager.services.FileUploadService import FileUploadService
from rest_framework import parsers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from data_extraction_manager.views.serializers.FileSerializer import FileSerializer
from django.conf import settings

class FileCSVView(GenericAPIView):
    # throttle_classes = ()
    # permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    # renderer_classes = (renderers.JSONRenderer,)
    serializer_class = FileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file_path = FileUploadService.handle_uploaded_file(serializer.validated_data["resume"],
                                                               settings.TEMPORAL_CSV_FILE_EXTENSION)
            FileUploadService.load_data_from_csv_file(file_path)
            return Response({"success": "True"}, status=status.HTTP_200_OK)
        return Response({'success': "False"}, status=status.HTTP_400_BAD_REQUEST)


class FileAvroView(GenericAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    serializer_class = FileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            file_path = FileUploadService.handle_uploaded_file(serializer.validated_data["resume"],
                                                               settings.TEMPORAL_AVRO_FILE_EXTENSION)
            FileUploadService.load_data_from_avro_file(file_path)
            return Response({"success": "True"}, status=status.HTTP_200_OK)
        return Response({'success': "False"}, status=status.HTTP_400_BAD_REQUEST)
