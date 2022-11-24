import django_tables2 as tables
from .models import Passenger, Ticket, Stop, Station, Trip, Train, Personnel, Address

class PassengerTable(tables.Table):
    class Meta:
        model = Passenger
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class TicketTable(tables.Table):
    class Meta:
        model = Ticket
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class StopTable(tables.Table):
    class Meta:
        model = Stop
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class StationTable(tables.Table):
    class Meta:
        model = Station
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class TripTable(tables.Table):
    class Meta:
        model = Trip
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class TrainTable(tables.Table):
    class Meta:
        model = Train
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class PersonnelTable(tables.Table):
    class Meta:
        model = Personnel
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class AddressTable(tables.Table):
    class Meta:
        model = Address
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class PassengerTable2(tables.Table):
    class Meta:
        model = Passenger
        fields = ("id","first_name",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}