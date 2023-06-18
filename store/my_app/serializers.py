from rest_framework import serializers

from my_app.models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'title', 'price']