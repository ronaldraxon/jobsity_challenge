from django.contrib import admin
from trip_business.models.Region import Region
from trip_business.models.Datasource import Datasource


# Register your models here.
admin.site.register(Region)
admin.site.register(Datasource)