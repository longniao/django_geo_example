from django.test import TestCase
from .models import People
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db import models

class PeopleTestCase(TestCase):
    def setUp(self):
        People.objects.create(
            name='aaa',
            location=Point(11, 11),
            address='aaa address',
            city='aaa city',
        )
        People.objects.create(
            name='bbb',
            location=Point(12, 12),
            address='bbb address',
            city='bbb city',
        )
        People.objects.create(
            name='ccc',
            location=Point(20, 20),
            address='ccc address',
            city='ccc city',
        )

    def test_population(self):
        '''
        test population
        '''
        population = People.objects.filter(location__distance_lt=(Point(11, 11), Distance(km=10*100))).aggregate(models.Count('id'))['id__count']
        self.assertEqual(population, 'population')
