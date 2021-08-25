from django.urls import path

from data_query_manager.views.ReportView import ReportByPolygonView
from data_query_manager.views.ReportView import ReportByRegionView
from data_query_manager.views.ReportView import ReportBySimilarCoordinatesAndHourView

app_name = "data_query_manager"
urlpatterns = [
    path("query_by_polygon", ReportByPolygonView.as_view(), name="report_by_polygon"),
    path("query_by_region/<str:region_name>", ReportByRegionView.as_view(), name="report_by_region"),
    path("query_by_similarities", ReportBySimilarCoordinatesAndHourView.as_view(), name="report_by_similarities")
]
