from django.db import models

class Passenger(models.Model):
    class Meta:
        db_table = 'passenger'
    passenger_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)