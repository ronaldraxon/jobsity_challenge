"""
trip_business.services.DatasourceService.py
===========================================

"""
from trip_business.models.Datasource import Datasource


class DatasourceService:

    @staticmethod
    def get_all_datasources_as_dict():
        return {datasource.name: datasource for datasource in Datasource.objects.all()}
