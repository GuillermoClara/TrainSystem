from django.shortcuts import render
from dbmsops.models import Passenger, Ticket, Stop, Station, Trip, Train, Personnel, PassengerAddress, StationAddress
from dbmsops.tables import PassengerTable, TicketTable, StopTable, StationTable, TripTable, TrainTable, PersonnelTable, PassengerAddressTable, StationAddressTable, PassengerTable2
from django_tables2 import RequestConfig

db_tables = [
    {'tb_name': 'Passenger', 'tb_fields':'(ID, firstName, lastName, DoB)', 'tb_data': PassengerTable(Passenger.objects.all())},
    {'tb_name': 'Ticket',  'tb_fields':'(ID, passengerID, purchaseDate, expirationDate, isValid, fare)', 'tb_data': TicketTable(Ticket.objects.all())},
    {'tb_name': 'Stop','tb_fields':'(stopID, stopIndex, arrivalTime, departTime, stationID)', 'tb_data': StopTable(Stop.objects.all())},
    {'tb_name': 'Station','tb_fields':'(ID, stationName, addressID)', 'tb_data': StationTable(Station.objects.all())},
    {'tb_name': 'Trip','tb_fields':'(ID, distance, duration)', 'tb_data': TripTable(Trip.objects.all())},
    {'tb_name': 'Train','tb_fields':'(ID, model, year, type)', 'tb_data': TrainTable(Train.objects.all())},
    {'tb_name': 'Personnel','tb_fields':'(ID, firstName, lastname, DoB)', 'tb_data': PersonnelTable(Personnel.objects.all())},
    {'tb_name': 'PassengerAddress','tb_fields':'(ID, streetAddress, country, state, city, zip)', 'tb_data': PassengerAddressTable(PassengerAddress.objects.all())},
    {'tb_name': 'StationAddress','tb_fields':'(ID, streetAddress, country, state, city, zip)', 'tb_data': StationAddressTable(StationAddress.objects.all())}
]

members_and_queries = [
    {'member_name': 'Mr. A', 'query': 'SELECT id, first_name FROM passenger'},
    {'member_name': 'Mr. B', 'query': 'SELECT id, first_name FROM passenger'}
]

def index(request):
    return render(request, 'dbmsops/index.html', {'db_tables': db_tables})

def reports(request):
    return render(request, 'dbmsops/reports.html', {'members_and_queries': members_and_queries})

# Have to make changes once every member's query is finalized
def report_details(request, report_number):
    tb_data = PassengerTable2(Passenger.objects.raw(members_and_queries[report_number-1]['query']))
      # enable sorting
    RequestConfig(request).configure(tb_data)
    tb_data.paginate(page=request.GET.get('page', 1), per_page=2)
    return render(request, 'dbmsops/details.html', {'tb_data': tb_data, 'member_and_query': members_and_queries[report_number-1]})

def data_entry_form(request, table_name):
    
    for obj in db_tables:
        if obj['tb_name'].lower() == table_name:
            tb_data = obj['tb_data']
            tb_schema = obj['tb_name'] + obj['tb_fields']
            RequestConfig(request).configure(tb_data)
            tb_data.paginate(page=request.GET.get('page', 1), per_page=2)
            break
    error = 'None'
    if request.method == 'POST':
        query_set = request.POST
        error = form_validation_helper(query_set)

    return render(request, 'dbmsops/forms/form.html', {'tb_schema': tb_schema, 'tb_data': tb_data,
       'tb_name': table_name, 'form_submission_error': error})

def not_found_404_view(request, exception):
    return render(request, 'dbmsops/404.html')

def server_error_500_view(request):
    return render(request, 'dbmsops/500.html')

def form_validation_helper(query_set):
    error = 'None'
    for key in query_set:
        if key != 'csrfmiddlewaretoken':
            if key.startswith('Passenger_firstName'):
                new_passenger = Passenger(first_name=query_set['Passenger_firstName'], 
                    last_name=query_set['Passenger_lastName'], dob=query_set['Passenger_DOB'])
                try:
                    new_passenger.save()
                except Exception as err:
                    error = 'Error: ' + err
            elif key.startswith('Ticket_passengerID'):
                try:
                    existing_passenger = Passenger.objects.get(id=query_set['Ticket_passengerID'])
                    new_ticket = Ticket(passenger_id = existing_passenger, purchase_date=query_set['Ticket_purchaseDate'],
                        expiration_date=query_set['Ticket_expirationDate'], is_valid=query_set['Ticket_isValid'], fare=query_set['Ticket_fare'])
                    try:
                        new_ticket.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Passenger with ID of {id} does not exists'.format(id=query_set['Ticket_passengerID'])
            elif key.startswith('Station_stationName'):
                try:
                    existing_address = Address.objects.get(id=query_set['Station_addressID'])
                    new_station = Station(address_id=existing_address, station_name=query_set['Station_stationName'])
                    try:
                        new_station.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Address with ID of {id} does not exists'.format(id=query_set['Station_addressID'])
    return error