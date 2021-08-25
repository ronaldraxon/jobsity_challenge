from django.contrib.gis.geos import GEOSGeometry
import pandas as pd
from trip_business.models.Region import Region
from trip_business.models.Trip import Trip


def compose_weekly_average_report(selection_type, selector_value, report):
    return dict({"selection_type": selection_type, "selector_value": selector_value, "report": report})


class QueryService:

    @staticmethod
    def get_weekly_trips_average_by_polygon_selection(poligon_dictionary):
        dates_list = QueryService.get_trip_dates_by_polygon(GEOSGeometry(str(poligon_dictionary)))
        return compose_weekly_average_report("Polygon",
                                             str(poligon_dictionary),
                                             QueryService.calculate_average_per_week_with_dates_list(dates_list))

    @staticmethod
    def get_weekly_trips_average_by_region_selection(region_name):
        dates_list = QueryService.get_trip_dates_by_region(region_name)
        return compose_weekly_average_report("Region",
                                             region_name,
                                             QueryService.calculate_average_per_week_with_dates_list(dates_list))

    @staticmethod
    def get_trip_dates_by_polygon(polygon):
        trips_filtered = [trip for trip in Trip.objects.all().values("trip_datetime", "_trip_origin_coordinates")
                          if polygon.contains(trip.get("_trip_origin_coordinates"))]
        dates = []
        for key in trips_filtered:
            dates.append(key.get("trip_datetime").date())
        return dates

    @staticmethod
    def get_trip_dates_by_region(region_name):
        trips_dates = [trips for trips in Trip.objects.filter(region__name=region_name).values("trip_datetime")]
        dates = []
        for key in trips_dates:
            dates.append(key.get("trip_datetime").date())
        return dates

    def is_valid_region(region_name):
        return Region.objects.filter(name=region_name).exists()

    @staticmethod
    def calculate_average_per_week_with_dates_list(dates_list):
        dataframe = pd.DataFrame(dates_list, columns=['dates'])
        dataframe.reset_index(inplace=True)
        dataframe = dataframe.groupby('dates', as_index=False). \
            agg(trips_average=pd.NamedAgg(column="dates", aggfunc="count"))
        dataframe['week_number'] = QueryService.get_number_of_week(dataframe['dates'])
        dataframe = dataframe.groupby('week_number', as_index=False)['trips_average'].mean()
        return dataframe.to_dict(orient='records')

    @staticmethod
    def get_number_of_week(dataframe):
        week = []
        for data in dataframe:
            week.append(data.isocalendar()[1])
        return week

    @staticmethod
    def get_aggregated_trips_with_similarities():
        pass
