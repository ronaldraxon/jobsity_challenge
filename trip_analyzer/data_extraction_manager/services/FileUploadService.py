"""
data_extraction_manager.services.FileUploadService.py
=====================================================

"""
import csv
from trip_business.services.RegionService import RegionService
from trip_business.services.DatasourceService import DatasourceService
from trip_business.models.Region import Region
from trip_business.models.Datasource import Datasource
from trip_business.models.Trip import Trip
import os


class FileUploadService:

    @staticmethod
    def handle_uploaded_file(f):
        # TODO rearrange name of file
        file_path_name = 'C:/Users/famil/Documents/jobsitychallenge/jobsity_challenge/trip_analyzer/media/csv/temp.csv'
        with open(file_path_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_path_name

    @staticmethod
    def load_data_from_file(file_path):
        all_regions = RegionService.get_all_regions_as_dict()
        all_datasources = DatasourceService.get_all_datasources_as_dict()
        trips = []
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            next(data)
            for row in data:
                region_name = row[0]
                datasource_name = row[4]
                region = all_regions.get(region_name)
                datasource = all_datasources.get(datasource_name)
                if not region:
                    region = Region.objects.create(name=region_name)
                    all_regions[region.name] = region
                if not datasource:
                    datasource = Datasource.objects.create(name=datasource_name)
                    all_datasources[datasource.name] = datasource
                trip = Trip()
                trip.region = region
                trip.trip_origin_coordinates = row[1]
                trip.trip_destination_coordinates = row[2]
                trip.trip_datetime = row[3]
                trip.data_source = datasource
                trips.append(trip)
                if len(trips) > 5000:
                    Trip.objects.bulk_create(trips)
                    trips = []
            if trips:
                Trip.objects.bulk_create(trips)

        FileUploadService.delete_temp_file(file_path)

    @staticmethod
    def delete_temp_file(file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
