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
Before you go any further, make sure you have created a database and you have an user with access to that database and permissions to create and drop tables.

![db](https://user-images.githubusercontent.com/10122730/130889567-b08e7d82-2f88-4663-9087-afdab7d9a7e5.PNG)

Also you're going to need the credentials to create a connection (user password), database host address, port and the database name. These will be configured in the next section.

### Configuring settings.py file
As you know, is a bad practice to share an explicit configuration on a repository. In this case we're using environment variables to store those sensitive values.
The configuration you should take care of is the DATABASES dictionary. Here you should set those values you got on the previous section

```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}
```

### Executing migrations

Now that you have created a database and set the values in the "settings.py file". You can proceed with the migrations. Please use a console to go to the project's folder and activate the specific virtual environment you created before.

```
conda activate jsc
```

Then, proceed with the migrations creation

```
python manage.py makemigrations
```

and migrate to create the tables on the database

```
python manage.py migrate
```
Now that we have created the tables, lets create a super user to gain access to the application

### Create super admin in django

Before starting the application, lets create an user to have access.

```
python manage.py createsuperuser
```
Here you have to specify user's name, password and a email address.

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
