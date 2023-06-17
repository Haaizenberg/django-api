from django.shortcuts import render
from rest_framework import viewsets

from my_app.serializers import ProductSerializer
from my_app.models import Product

# Create your views here.
# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer