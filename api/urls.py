from django.urls import path

from .views import PeopleManageViewSet, PeopleStatisticViewSet


urlpatterns = [

    path('create/', PeopleManageViewSet.as_view({'post': 'create'}), name='api_people_create'),
    path('population/', PeopleStatisticViewSet.as_view({'post': 'population'}), name='api_people_population'),

]

