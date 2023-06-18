from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Car(ExportModelOperationsMixin('car'),models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
