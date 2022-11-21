import traceback

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db import models
from rest_framework import viewsets
from rest_framework.response import Response

from .message import result
from .models import People
from .serializers import PeopleCreateSerializer, PeopleStatisticSerializer


class PeopleManageViewSet(viewsets.ModelViewSet):
    '''
    People manage
    '''
    serializer_class = PeopleCreateSerializer

    def create(self, request):
        serializer = PeopleCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                location = Point(serializer.validated_data['latitude'], serializer.validated_data['longitude'])
                people = People.objects.create(
                    name=serializer.validated_data['name'],
                    location=location,
                    address=serializer.validated_data.get('address', ''),
                    city=serializer.validated_data.get('city', ''),
                )
                people.save()
                return Response(result(0))
            except Exception:
                print(traceback.format_exc())
                return Response(result(1))

        return Response(result(3), status=500)


class PeopleStatisticViewSet(viewsets.ModelViewSet):
    '''
    People statistic
    '''
    serializer_class = PeopleStatisticSerializer

    def population(self, request):
        serializer = PeopleStatisticSerializer(data=request.data)
        if serializer.is_valid():
            try:
                location = Point(serializer.validated_data['latitude'], serializer.validated_data['longitude'])
                radius = serializer.validated_data['radius']
                # peoples = People.objects.only('id').filter(location__distance_lt=(location, Distance(km=radius*100))).count()
                # serializer = PeoplePopulationSerializer(peoples)
                # return Response(serializer.data)
                population = People.objects.filter(location__distance_lt=(location, Distance(km=radius*100))).aggregate(models.Count('id'))['id__count']
                return Response({'population':population})
            except Exception:
                print(traceback.format_exc())
                return Response(result(1))

        return Response(result(2))

