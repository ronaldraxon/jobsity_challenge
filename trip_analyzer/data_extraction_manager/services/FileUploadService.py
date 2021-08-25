import csv
from trip_business.services.RegionService import RegionService
from trip_business.services.DatasourceService import DatasourceService
from trip_business.models.Region import Region
from trip_business.models.Datasource import Datasource
from trip_business.models.Trip import Trip
from django.conf import settings
import os
from datetime import datetime
from fastavro import reader

class FileUploadService:

    @staticmethod
    def create_temporal_file_path(extension):
        return settings.UPLOADED_FILES_PATH + \
               settings.TEMPORAL_FILE_PREFIX + \
               str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S")) + \
               extension

    @staticmethod
    def handle_uploaded_file(f,extension):
        file_path_name = FileUploadService.create_temporal_file_path(extension)
        with open(file_path_name, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_path_name

    @staticmethod
    def load_data_from_csv_file(file_path):
        all_regions, all_datasources = FileUploadService.get_regions_and_datasources()
        trips = []
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=settings.FILE_DELIMITER)
            next(data)
            for row in data:
                region_name = row[0]
                datasource_name = row[4]
                region = FileUploadService.create_region_instance(region_name, all_regions)
                datasource = FileUploadService.create_datasource_instance(datasource_name, all_datasources)
                trips.append(FileUploadService.create_trip_instance(row[1], row[2], row[3], region, datasource))
                FileUploadService.trip_bulk_creation(trips)
            FileUploadService.bulk_remaining_trips(trips)
        FileUploadService.delete_temp_file(file_path)

    @staticmethod
    def load_data_from_avro_file(file_path):
        all_regions, all_datasources = FileUploadService.get_regions_and_datasources()
        trips = []
        with open(file_path, 'rb') as fo:
            for record in reader(fo):
                region_name = record.get("region")
                datasource_name = record.get("datasource")
                region = FileUploadService.create_region_instance(region_name, all_regions)
                datasource = FileUploadService.create_datasource_instance(datasource_name, all_datasources)
                trips.append(FileUploadService.create_trip_instance(record.get("origin_coord"),
                                                                    record.get("destination_coord"),
                                                                    record.get("datetime"),
                                                                    region, datasource))
                FileUploadService.trip_bulk_creation(trips)
            FileUploadService.bulk_remaining_trips(trips)
        FileUploadService.delete_temp_file(file_path)

    @staticmethod
    def trip_bulk_creation(trips):
        if len(trips) > 100000:
            Trip.objects.bulk_create(trips, ignore_conflicts=True)
            trips = []

    @staticmethod
    def bulk_remaining_trips(trips):
        if trips:
            Trip.objects.bulk_create(trips, ignore_conflicts=True)

    @staticmethod
    def get_regions_and_datasources():
        return RegionService.get_all_regions_as_dict(), DatasourceService.get_all_datasources_as_dict()

    @staticmethod
    def create_trip_instance(origin_coordinates, destination_coordinates, date_time, region, datasource):
        trip = Trip()
        trip.region = region
        trip.trip_origin_coordinates = origin_coordinates
        trip.trip_destination_coordinates = destination_coordinates
        trip.trip_datetime = date_time
        trip.data_source = datasource
        return trip

    @staticmethod
    def create_region_instance(region_name, all_regions_dictionary):
        region = all_regions_dictionary.get(region_name)
        if not region:
            region = Region.objects.create(name=region_name)
            all_regions_dictionary[region.name] = region
        return region

    @staticmethod
    def create_datasource_instance(datasource_name, all_datasources_dictionary):
        datasource = all_datasources_dictionary.get(datasource_name)
        if not datasource:
            datasource = Datasource.objects.create(name=datasource_name)
            all_datasources_dictionary[datasource.name] = datasource
        return datasource

    @staticmethod
    def delete_temp_file(file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
