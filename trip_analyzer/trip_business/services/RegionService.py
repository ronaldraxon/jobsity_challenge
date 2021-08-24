"""
trip_business.services.RegionService.py
=======================================

"""
from trip_business.models.Region import Region


class RegionService:

    @staticmethod
    def get_all_regions():
        return {region.region_name: region for region in Region.objects.all()}
