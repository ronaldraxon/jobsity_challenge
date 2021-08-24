# Jobsity data ingestion challenge

## Introduction



## Instalation Requirements


### Hardware

* Intel o AMD de 4 núcleos, 3.0 Ghz or superior
* RAM 16 GB (8 Libres)
* DD 50MB

### Database

* postgresql 13 
* postGIS 3.1 - You can install this from stack builder 4.2.1 (https://postgis.net/windows_downloads/)

create an spatial database

conda install -c conda-forge gdal
conda install -c conda-forge djangorestframework

https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/


install requirementes postgis
https://postgis.net/docs/postgis_installation.html#install_requirements

### Create super admin in django
python manage.py createsuperuser

conda create --name jsc python=3.8
conda install -c anaconda django
conda install -c conda-forge gdal
conda install -c conda-forge djangorestframework
