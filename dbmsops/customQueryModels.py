from django.db import models

class Query1Model(models.Model):
    passenger_id = models.IntegerField()

class Query2Model(models.Model):
    amount = models.FloatField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)