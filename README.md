# Django Geo Example

A example for Django + PostgreSQL + PostGIS


# Installation

**1. Install PostgreSQL**

**2. Install PostGIS**

**3. Creating A Spatial Database**

```
createdb geo_example
psql geo_example
CREATE EXTENSION postgis;
```

**4. Clone Repository**

```
git clone git@github.com:longniao/django_geo_example.git
```

**5. Install Dependencies**

```
pip install -r requirements.txt
```

**6. Config Database**

```
# geo/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geo_example',
        'USER': 'username',		# your username
        'PASSWORD': 'password',	# your password
        'HOST': 'localhost',
        'PORT': '5432'
    },
}
```

**7. Migrate Database**

```
python manage.py migrate
```

**8. Run Server**

```
python manage.py runserver
```


# Usage

1. Create people with name, latitude, longitude, address, city fields via: [http://127.0.0.1:8000/api/create/](http://127.0.0.1:8000/api/create/)

2. Get the population living in the area of a certain location and radius. [http://127.0.0.1:8000/api/population/](http://127.0.0.1:8000/api/population/)


# Issues

If you have any issues, please use [GitHub's issues](https://github.com/longniao/django_geo_example/issues).

