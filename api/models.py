from django.contrib.gis.db import models

class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
