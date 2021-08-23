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

from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.shortcuts import redirect
from django.contrib import admin
from rest_framework import permissions

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('upload/', include('data_extraction_manager.urls')),
#]

def root_redirect(request):
    return redirect('trip_analyzer/admin/')


services_urlpatterns = [
    url(r"^trip_analyzer/data_extraction_manager/", include("data_extraction_manager.urls", namespace="data-extraction-manager-urls"))
]


urlpatterns = [
                  url(r'^trip_analyzer/admin/', admin.site.urls, name='application-administration-urls'),
                  url(r'^$', root_redirect),
              ] + services_urlpatterns

#if settings.DEBUG:
#  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)