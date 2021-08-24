"""
trip_business.services.RegionService.py
=======================================

"""
from trip_business.models.Region import Region


class RegionService:

    @staticmethod
    def get_all_regions_as_dict():
        return {region.name: region for region in Region.objects.all()}
