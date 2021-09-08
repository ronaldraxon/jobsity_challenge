# Jobsity data ingestion challenge

## Installation Requirements


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
conda install -c anaconda gdal=3.0.2
```

You can use the **environment_<your_Os_Here>.yml** file to create the virtual environment.

### windows:
```
conda env create -f environment_Windows.yml
```

### Linux:
```
conda env create -f environment_Linux.yml
```

If you experience any problem when creating the virtual environment, you can use the package installation lines. 
A full list of installation commands (suitable for linux and windows) for your virtual environment will be as follows (all of these using conda as environment and package manager):

```
conda create --name jsc python=3.8
conda activate jsc
conda install -c anaconda django=3.1.2
conda install -c conda-forge djangorestframework=3.12.4
conda install -c conda-forge django-environ=0.4.5
conda install -c conda-forge drf-yasg=1.20.0
conda install -c conda-forge djangorestframework_simplejwt=4.4.0
conda install -c anaconda pandas=1.1.3
conda install -c conda-forge fastavro=1.4.4
conda install -c anaconda gdal=3.0.2
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

You can configure environment variables on you virtual environment. Please use the following commands
to set the database environment variables. Be sure to activate the previous created virtual environment and to set a valid value for each one of the following commands

```
conda env config vars set DB_NAME=<YOUR-DATABASE-NAME-HERE>
conda env config vars set DB_USERNAME=<YOUR-DATABASE-USERNAME-NAME-HERE>
conda env config vars set DB_PASSWORD=<YOUR-DATABASE-PASSWORD-HERE>
conda env config vars set DB_HOST=<YOUR-DATABASE-HOST-ADDRESS-HERE>
conda env config vars set DB_PORT=<YOUR-DATABASE-PORT-HERE>
```
After you created the varibles please deactivate and activate the virtual environment to make your changes take effect.

```
conda deactivate
conda activate jsc
```
You can now list your varibles. 
```
conda env config vars list
```
You're going to see something like this.
![environmentvars](https://user-images.githubusercontent.com/10122730/132461031-d7f1ef8d-dc2d-49b0-a4f3-909959b2ff83.PNG)


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
There you have to specify user's name, password and a email address. After you create an user you can run the aplication by typing:

```
python manage.py runserver
```
![running](https://user-images.githubusercontent.com/10122730/132461101-d89c9095-1778-4be9-afa0-381b1e7399d9.PNG)


## Using the application

After you start the application, you can use a web browser (Google Chrome or Firefox) and type the following url in the url bar and press enter.
http://127.0.0.1:8000



A web page is going to show up, asking for the superuser credentials you just created before. Plase type them to login

![admin](https://user-images.githubusercontent.com/10122730/130891890-7c3aa1f6-9ebc-483d-a84e-d36a3e500770.PNG)

Once you're authenticated, please go to the following url:

http://127.0.0.1:8000/trip_analyzer/swagger/

### Swagger 

Swagger is a well positioned and user friendly set of tools to interact and document with the REST API endpoints (https://swagger.io/).

![swagger](https://user-images.githubusercontent.com/10122730/130892390-8368fa0c-efa9-4ee1-a8e8-577d84f951aa.PNG)

For this project we're using the package drf-yasg to implement swagger functionalities on Django.

### File Upload

For data loading purposes, I have posted some testing files on Google Drive:
https://drive.google.com/drive/folders/1k92P_qPmUTXq5SEHscu40nmPaqGCM0rQ?usp=sharing

There you're going to find the following files:

* trips.csv: Contains 100 trip records for high demanding testing(13kb).
* coord_trips.csv: Contains 100.000.000 trip records for high demanding testing (12.7GB).
* coord_trips.avro: Contains the same data included in coord_trips.csv (100.000.000 records), but with a considerable amount of compression (390MB).

You can use the endpoint http://127.0.0.1:8000/trip_analyzer/data_extraction_manager/csvfileupload to upload csv files. Nevertheless, for compressed files 
containing a large amount of data, it is preferred to use avro files. In that case, please use the endpoint http://127.0.0.1:8000/trip_analyzer//data_extraction_manager/avrofileupload.

![FileUpload](https://user-images.githubusercontent.com/10122730/130895012-7b19db37-aaeb-4721-a341-3a5897efb678.PNG)

Keep in mind that you can use the csv endpoint to upload big files, but is not going to perform well in comparison to the avro option.

### Reports

#### By specifying a bounding box via Polygon object 

You can use the following url and body to extract a report by defining a bounding box (or polygon in this case):

http://127.0.0.1:8000/trip_analyzer/data_query_manager/query_by_polygon

```
{
  "type": "Polygon",
  "coordinates": [
    [[7.000,  50.000], [7.000, 54.000], [15.000, 54.000], [15.000, 50.000], [7.000,  50.000]]
  ]
}
```

![byPoly](https://user-images.githubusercontent.com/10122730/130893449-afbf816b-c986-4cbf-a676-cd196a6181d1.PNG)


**Response example:**

```
{
  "selection_type": "Polygon",
  "selector_value": "{'type': 'Polygon', 'coordinates': [[[7.0, 50.0], [7.0, 54.0], [15.0, 54.0], [15.0, 50.0], [7.0, 50.0]]]}",
  "report": [
    {
      "week_number": 18,
      "trips_average": 2
    },
    {
      "week_number": 19,
      "trips_average": 1
    },
    {
      "week_number": 20,
      "trips_average": 2
    },
    {
      "week_number": 21,
      "trips_average": 2
    },
    {
      "week_number": 22,
      "trips_average": 2
    }
  ]
}
```

#### By specifying a region

You can also, use the parametric url to get a report by region:

http://127.0.0.1:8000/trip_analyzer/data_query_manager/query_by_region/region_name

![byRegion](https://user-images.githubusercontent.com/10122730/130893565-df53aedd-00f8-4393-b281-d93993c2547c.PNG)

```
{
  "selection_type": "Region",
  "selector_value": "Prague",
  "report": [
    {
      "week_number": 18,
      "trips_average": 2
    },
    {
      "week_number": 19,
      "trips_average": 1
    },
    {
      "week_number": 20,
      "trips_average": 1
    },
    {
      "week_number": 21,
      "trips_average": 1
    },
    {
      "week_number": 22,
      "trips_average": 1
    }
  ]
}
```

