from rest_framework import serializers


class PeopleCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    address = serializers.CharField(max_length=100, required=False)
    city = serializers.CharField(max_length=50, required=False)

class PeopleStatisticSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    radius = serializers.FloatField()
    city = serializers.CharField(max_length=50, required=False)
