# Jobsity data ingestion challenge

## Introduction



## Instalation Requirements


* Anaconda (https://www.anaconda.com/)
  * conda or miniconda for virtual environment management.
  * conda as package manager.
* Python 3.8.
* Django 3.1
* PostgreSQL V.13 database (https://www.postgresql.org/download/).
  * You may need pgAdmin as UI to manage databases and users.
* PostGIS 3.1 for PostgreSQL (Extension for GIS or spatil Databases). You can install this from stack builder 4.2.1 (https://postgis.net/windows_downloads/).

You have to install the previous extension (PostGIS 3.1) on your database before attempting any creation of a new databse. Also, you have to install the respective packages by including the following command to you package instalation plan:

```
conda install -c conda-forge gdal
```

A full list of installation commands list for your virtual environment will be as follows (all of these using conda as environment and package manager):

```
conda create --name jsc python=3.8
conda install -c anaconda django
conda install -c conda-forge gdal
conda install -c conda-forge djangorestframework
conda install -c conda-forge drf-yasg
conda install -c conda-forge djangorestframework_simplejwt
conda install -c anaconda pandas
conda install -c conda-forge fastavro
```
Also, you can use the **environment.yaml** file to create the virtual environment.

```
conda env create -f environment.yml
```

You can see the requirements for postgis in django and additional installation requirementes on the following links:
   * https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/postgis/
   * https://postgis.net/docs/postgis_installation.html#install_requirements   

Notice you dont need to follow the instructions on the previous links to execute the application. This was added just for reference.

## Setting the development environment

### Database creation

### Configuring settings.py file

### Executing migrations

### Create super admin in django
python manage.py createsuperuser

## Using the application

### Swagger 

### File Upload

### Reports

#### By specifying a bounding box via Polygon object 

```
{
  "type": "Polygon",
  "coordinates": [
    [[7.000,  50.000], [7.000, 54.000], [15.000, 54.000], [15.000, 50.000], [7.000,  50.000]]
  ]
}
```
