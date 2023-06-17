from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Product(ExportModelOperationsMixin('product'),models.Model):
    # product_id = models.UUIDField(primary_key=True)
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    # created_at = models.DateTimeField()
    def __str__(self):
        return self.name
