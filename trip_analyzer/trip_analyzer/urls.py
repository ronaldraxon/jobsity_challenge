"""trip_analyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import include
from django.conf.urls import url
from django.shortcuts import redirect
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from trip_business.models.Region import Region
from trip_business.models.Datasource import Datasource
from trip_business.models.Trip import Trip

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('upload/', include('data_extraction_manager.urls')),
#]

schema_view = get_schema_view(
    openapi.Info(
        title="Trip Analizer",
        default_version='v1.0.0',
        description="""This is a challenge Project.""",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@tripanalyzer.local"),
        license=openapi.License(name="Open License"),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)


def root_redirect(request):
    return redirect('trip_analyzer/admin/')


services_urlpatterns = [
    url(r"^trip_analyzer/data_extraction_manager/", include("data_extraction_manager.urls", namespace="data-extraction-manager-urls")),
    url(r"^trip_analyzer/trip_business/", include("trip_business.urls", namespace="trip-business-urls")),
    url(r"^trip_analyzer/data_query_manager/", include("data_query_manager.urls", namespace="data-query-manager-urls"))
]


urlpatterns = [
                  url(r'^trip_analyzer/admin/', admin.site.urls, name='application-administration-urls'),
                  url(r'^trip_analyzer/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  url(r'^$', root_redirect),

              ] + services_urlpatterns

#if settings.DEBUG:
#  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)