from rest_framework import serializers

from my_app.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price']