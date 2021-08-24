from django.urls import path


from data_query_manager.views.SelectionByPoligonView import SelectionByPolygonView

app_name = "data_query_manager"
urlpatterns = [
    path('querybypolygon', SelectionByPolygonView.as_view(), name="selection_by_polygon")
]