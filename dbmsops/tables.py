import django_tables2 as tables
from .models import Passenger, Ticket, Stop, Station, Trip, Train, Personnel, PassengerAddress, StationAddress, WorkRoster, ScheduledOn
from dbmsops.customQueryModels import Query1Model, Query2Model, Query3Model, Query4Model

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

class PassengerAddressTable(tables.Table):
    class Meta:
        model = PassengerAddress
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class StationAddressTable(tables.Table):
    class Meta:
        model = StationAddress
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class WorkRosterTable(tables.Table):
    class Meta:
        model = WorkRoster
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class ScheduledOnTable(tables.Table):
    class Meta:
        model = ScheduledOn
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}
        
class PassengerTable2(tables.Table):
    class Meta:
        model = Passenger
        fields = ("id","first_name",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

# Reports query tables #

class Query1Table(tables.Table):
    class Meta:
        model = Query1Model
        fields = ("passenger_id",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class Query2Table(tables.Table):
    class Meta:
        model = Query2Model
        fields = ("first_name", "last_name", "amount",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class Query3Table(tables.Table):
    class Meta:
        model = Query3Model
        fields = ("full_name", "no_of_tickets",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}

class Query4Table(tables.Table):
    class Meta:
        model = Query4Model
        fields = ("station_name", "no_of_trains",)
        attrs = {"class": "table table-container table-hover", "thead": {"class": "table-primary"}}