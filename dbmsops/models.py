from django.db import models

class Train(models.Model):
    class Meta:
        db_table = 'train'
    model = models.CharField(max_length=50)
    year = models.IntegerField()


class Personnel(models.Model):
    class Meta:
        db_table = 'personnel'
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    dob = models.DateField()


class Address(models.Model):
    class Meta:
        db_table = 'address'
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)


class Passenger(models.Model):
    class Meta:
        db_table = 'passenger'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_id = models.ForeignKey(Address, default=None, on_delete=models.DO_NOTHING)


class Station(models.Model):
    class Meta:
        db_table = "station"
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=50)


class Stop(models.Model):
    class Meta:
        db_table = "stop"
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_index = models.IntegerField(default=0)


class Route(models.Model):
    class Meta:
        db_table = "route"
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_max_speed = models.IntegerField(default=0)


class Trip(models.Model):
    class Meta:
        db_table = "trip"
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    travels_on = models.ForeignKey(Train, on_delete=models.CASCADE)
    date = models.DateField()


class Ticket(models.Model):
    class Meta:
        db_table = "ticket"
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    expiration_date = models.DateField()
    price = models.IntegerField(default=0)


class AffiliatedWith(models.Model):
    class Meta:
        db_table = "affiliatedWith"
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    route_index = models.IntegerField(default=0)


class ScheduledOn(models.Model):
    class Meta:
        db_table = "scheduledOn"

    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    date_time = models.DateTimeField()


class WorkRoster(models.Model):
    class Meta:
        db_table = "workRoster"
    personnel_id = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    since = models.DateField()

