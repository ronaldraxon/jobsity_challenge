from django.contrib.gis.geos import GEOSGeometry

class QueryService:

    @staticmethod
    def get_weekly_trips_average_by_polygon_selection(poligon_dictionary):
        print(dict(poligon_dictionary))
        print(type(dict(poligon_dictionary)))
        print(GEOSGeometry(str(poligon_dictionary)))