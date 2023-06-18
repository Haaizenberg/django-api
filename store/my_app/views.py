from django.shortcuts import render
from rest_framework import viewsets

from my_app.serializers import CarSerializer
from my_app.models import Car

# Create your views here.
# ViewSets define the view behavior.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer