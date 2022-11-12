from django.db import models

class Passenger(models.Model):
    passenger_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)