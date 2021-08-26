# Jobsity data ingestion challenge

## Introduction



## Instalation Requirements

conda or miniconda or virtualenv for virtual environment management
pip or conda as package managers
python 3.8+
PostgreSQL V.13 database
  * You may need pgAdmin as UI to manage databases and users
PostGIS 3.1 for PostgreSQL (Extension for GIS or spatil Databases) - You can install this from stack builder 4.2.1 (https://postgis.net/windows_downloads/)

You have to install the previous extension on your database before attempting any creation of a new databse. Also, you have to install the respective packages by including the following command to you package instalation plan:

conda install -c conda-forge gdal

A full list of installation commands for your virtual environment will be as follows (all of these using conda as environment and package manager):

conda create --name jsc python=3.8
conda install -c anaconda django
conda install -c conda-forge gdal
conda install -c conda-forge djangorestframework
conda install -c conda-forge drf-yasg
conda install -c conda-forge djangorestframework_simplejwt
conda install -c anaconda pandas
conda install -c conda-forge fastavro

You can see the requirements for postgis in django and additional installation requirementes on the following links:
   * https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/
   * https://postgis.net/docs/postgis_installation.html#install_requirements   




conda install -c conda-forge djangorestframework

https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/


install requirementes postgis


### Create super admin in django
python manage.py createsuperuser


{
  "type": "Polygon",
  "coordinates": [
    [[0.0, 0.0], [0.0, 50.0], [50.0, 50.0], [50.0, 0.0], [0.0, 0.0]]
  ]
}
