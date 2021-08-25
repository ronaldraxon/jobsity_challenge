from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from data_query_manager.views.serializers.WeeklyAverageReportSerializer import WeeklyAverageReportSerializer
from data_query_manager.views.serializers.PolygonSelectionSerializer import PolygonSelectionSerializer
from data_query_manager.views.serializers.ReportBySimilaritiesSerializer import ReportBySimilaritiesSerializer
from data_query_manager.services.QueryService import QueryService


class ReportByPolygonView(generics.GenericAPIView):
    serializer_class = PolygonSelectionSerializer

    @staticmethod
    @method_decorator(decorator=swagger_auto_schema(
        operation_description="Generates a report containing the average of trips in a week.",
        responses={
            201: openapi.Response('Successful request', WeeklyAverageReportSerializer),
            400: openapi.Response('Failed request'),
        }))
    def post(request):
        request_serializer = PolygonSelectionSerializer(data=request.data)
        if request_serializer.is_valid():
            response = QueryService.get_weekly_trips_average_by_polygon_selection(request_serializer.data)
            return Response(WeeklyAverageReportSerializer(response).data, status=status.HTTP_200_OK)
        else:
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportByRegionView(generics.GenericAPIView):
    serializer_class = WeeklyAverageReportSerializer
    param = openapi.Parameter('region_name', openapi.IN_PATH,
                              description="The region name to use as a filter to generate the report",
                              type=openapi.TYPE_STRING,
                              required=True)

    @staticmethod
    @method_decorator(decorator=swagger_auto_schema(
        operation_description="Generates a report containing the average of trips in a week.",
        manual_parameters=[param],
        responses={
            200: openapi.Response('Successful request', WeeklyAverageReportSerializer),
            400: openapi.Response('Failed request'),
        }))
    def get(request, region_name):
        if QueryService.is_valid_region(region_name):
            response = QueryService.get_weekly_trips_average_by_region_selection(region_name)
            return Response(WeeklyAverageReportSerializer(response).data, status=status.HTTP_200_OK)
        else:
            return Response('Failed request', status=status.HTTP_400_BAD_REQUEST)


class ReportBySimilarCoordinatesAndHourView(generics.GenericAPIView):
    serializer_class = ReportBySimilaritiesSerializer

    @staticmethod
    @method_decorator(decorator=swagger_auto_schema(
        operation_description="Generates an aggregated report with similar origin, destination and trip hour of day.",
        responses={
            200: openapi.Response('Successful request', ReportBySimilaritiesSerializer),
            400: openapi.Response('Failed request'),
        }))
    def get(request):
        logger.info("Obtener solicitud {}".format(year))

        if True:
            return Response('Successful request', status=status.HTTP_200_OK)
        else:
            return Response('Failed request', status=status.HTTP_400_BAD_REQUEST)
