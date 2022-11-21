import django_tables2 as tables
from .models import Passenger

class PassengerTable(tables.Table):
    class Meta:
        model = Passenger
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class PassengerTable2(tables.Table):
    class Meta:
        model = Passenger
        fields = ("id","first_name",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}
