from django.db import models

# Create your models here.


class Buses(models.Model):
    bus_id = models.IntegerField(primary_key=True)
    area_from = models.CharField(max_length=150, blank=True, null=True)
    area_to = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'buses'