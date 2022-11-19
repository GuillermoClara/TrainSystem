import django_tables2 as tables
from .models import Passenger

class PassengerTable(tables.Table):
    class Meta:
        model = Passenger
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}