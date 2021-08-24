
from rest_framework import status
from django.http import HttpResponse
from django.views.generic.edit import FormView
from data_extraction_manager.forms.FileUploadForm import FileUploadForm
from data_extraction_manager.services.FileUploadService import FileUploadService
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from django.utils.decorators import method_decorator
from data_query_manager.views.serializers.PolygonSelectionSerializer import PolygonSelectionSerializer
from data_query_manager.services.QueryService import QueryService

class SelectionByPolygonView(generics.GenericAPIView):

    serializer_class = PolygonSelectionSerializer

    @staticmethod
    @method_decorator(decorator=swagger_auto_schema(
        operation_description="""Este endpoint crea un nuevo punto de tipo cajero electrónico. """,
        responses={
            201: openapi.Response('¡Successfull request!'),
            400: openapi.Response('¡Error in the request!'),
        }))
    def post(request):
        """Selección de viajes a partir de un conjunto de puntos.
        - **parameters**::
              :param request: Cuerpo de la solicitud.

        - **return**::
              :return: Punto con codigo de estado 201 (Creado).
        """
        request_serializer = PolygonSelectionSerializer(data=request.data)

        if request_serializer.is_valid():
            QueryService.get_weekly_trips_average_by_polygon_selection(request_serializer.data)
            #response = BusinessUnitService.create_new_business_unit(business_unit_data=request_serializer)
            return Response('Consulta creada de forma satisfactoria',
                            status=status.HTTP_201_CREATED)
        else:
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
