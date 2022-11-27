from django.shortcuts import render
from dbmsops.models import Passenger, Ticket, Stop, Station, Trip, Train, Personnel, PassengerAddress, StationAddress, WorkRoster, ScheduledOn
from dbmsops.tables import PassengerTable, TicketTable, StopTable, StationTable, TripTable, TrainTable, PersonnelTable, PassengerAddressTable, StationAddressTable, WorkRosterTable, ScheduledOnTable, Query1Table, Query2Table, Query3Table, Query4Table, Query5Table, Query6Table, Query7Table, Query8Table, Query9Table, Query10Table
from dbmsops.customQueryModels import Query1Model, Query2Model, Query3Model, Query4Model, Query5Model, Query6Model, Query7Model, Query8Model, Query9Model
from django_tables2 import RequestConfig
from django.db import connection

db_tables = {
    'passenger': {'tb_name': 'Passenger', 'tb_fields':'(ID, firstName, lastName, DoB)', 'passengerTable': PassengerTable, 'passengerModel': Passenger},
    'ticket': {'tb_name': 'Ticket',  'tb_fields':'(ID, passengerID, tripID, purchaseDate, expirationDate, isValid, fare)', 'ticketTable':  TicketTable, 'ticketModel': Ticket},
    'stop':{'tb_name': 'Stop','tb_fields':'(stopID, stationID, tripID, routeIndex, arrivalTime, departureTime, date)', 'stopTable': StopTable, 'stopModel': Stop},
    'station':{'tb_name': 'Station','tb_fields':'(ID, stationName, builtYear)', 'stationTable': StationTable, 'stationModel': Station},
    'trip':{'tb_name': 'Trip','tb_fields':'(ID, trainID, date, distance, duration)', 'tripTable': TripTable, 'tripModel': Trip},
    'train':{'tb_name': 'Train','tb_fields':'(ID, model, year, type)', 'trainTable': TrainTable, 'trainModel': Train},
    'personnel':{'tb_name': 'Personnel','tb_fields':'(ID, firstName, lastname, DoB)', 'personnelTable': PersonnelTable, 'personnelModel': Personnel},
    'passengeraddress':{'tb_name': 'PassengerAddress','tb_fields':'(ID, passengerID, streetAddress, country, state, city, zip)', 'passengeraddressTable': PassengerAddressTable, 'passengeraddressModel': PassengerAddress},
    'stationaddress':{'tb_name': 'StationAddress','tb_fields':'(ID, stationID, streetAddress, country, state, city, zip)', 'stationaddressTable': StationAddressTable, 'stationaddressModel': StationAddress},
    'workroster':{'tb_name': 'WorkRoster','tb_fields':'(ID, personnelID, trainID, role, workDate)', 'workrosterTable': WorkRosterTable, 'workrosterModel': WorkRoster},
    'scheduledon':{'tb_name': 'ScheduledOn','tb_fields':'(ID, stationID, tripID, dateTime)', 'scheduledonTable': ScheduledOnTable, 'scheduledonModel': ScheduledOn},
}

members_and_queries = [
    {'query_name': 'Get all passengerIDs that have arrived to station 10 after 1999, any time between 8:00 AM to 9:00 PM.',
    'query': """
        SELECT ticket.passenger_id_id
        FROM ticket 
        JOIN stop ON ticket.trip_id_id = stop.trip_id_id
        WHERE stop.station_id_id = 10 AND
        stop.date > '12/31/1999' AND
        stop.arrival_time >= '08:00:00' AND
        stop.arrival_time <= '17:00:00';
    """},
    {'query_name': 'Get the top 10 passenger names and amount that have spent more than $12.00 between 31 Jan 2022 and 31 Dec 2022.', 
    'query': """ 
        SELECT Passenger.first_name, Passenger.last_name, SUM(Ticket.fare) as amount 
        FROM Passenger, Ticket
        WHERE Passenger.id=Ticket.passenger_id_id AND Ticket.purchase_date > '01/31/2022' AND Ticket.purchase_date <= '12/31/2022'
        GROUP BY Passenger.id 
        HAVING SUM(Ticket.fare) > 12.00 
        ORDER BY SUM(Ticket.fare) DESC LIMIT 10;
        """ },
    {'query_name': 'Find all passengers and their ticketCount having highest number of tickets purchased between 19 Jan 2022 to 24 Aug 2022.', 
    'query': """ 
        SELECT Passenger.first_name || ' ' || Passenger.last_name as full_name, COUNT(Ticket.id) as number_of_tickets 
        FROM Ticket, Passenger 
        WHERE Ticket.passenger_id_id=Passenger.id AND Ticket.purchase_date > '01-19-2022' AND Ticket.purchase_date < '08-24-2022'
        GROUP BY Passenger.id 
        ORDER BY COUNT(Ticket.id) DESC;
        """ },
     {'query_name': 'Find all the stations and number of trains sorted in descending order.', 
    'query': """ 
        SELECT Station.station_name, COUNT(so.id) as no_of_trains
        FROM scheduled_on as so, Station 
        WHERE so.station_id_id = Station.id
        GROUP BY Station.id
        ORDER BY COUNT(so.id) DESC;
        """ },
    {'query_name': 'For all trip ids, find the number of stops for each of those trips.', 
    'query': """ 
        SELECT COUNT(stop.id) as no_of_stops, stop.trip_id_id as trip_id
        FROM stop, trip
        WHERE stop.trip_id_id = trip.id
        GROUP BY stop.trip_id_id;
        """ },
    {'query_name': 'For train id 4, find the personnel names and their id working on the train from 1 April 2022 to 3 Dec 2022.', 
    'query': """ 
        SELECT personnel.first_name || ' ' || personnel.last_name as full_name, personnel.id as personnel_id
        FROM work_roster, personnel 
        WHERE train_id_id = 4 AND personnel.id = work_roster.personnel_id_id 
            AND work_roster.work_date >= '04-01-2022' AND work_roster.work_date <= '12-03-2022'
        Group BY work_roster.train_id_id, personnel.id;
        """ },
    {'query_name': 'Get the number of passengers that have traveled to a station in Georgia.', 
    'query': """ 
        SELECT COUNT(*) as no_of_passengers
        FROM ticket, trip
        WHERE trip.id = ticket.trip_id_id
        AND trip.id IN (
            SELECT trip.id
            FROM trip, stop, station_address
            WHERE stop.trip_id_id = trip.id
            AND stop.station_id_id = station_address.station_id
            AND station_address.state = 'Georgia'
        );
        """ },
    {'query_name': 'Find the passengers that have traveled on a train in the same state that they live in.', 
    'query': """ 
        SELECT distinct passenger.id as passenger_id, passenger_address.state
        FROM ticket, passenger, trip, stop, passenger_address, station_address
        WHERE ticket.passenger_id_id = passenger.id
        AND station_address.station_id = stop.station_id_id
        AND ticket.trip_id_id = trip.id
        AND stop.trip_id_id = trip.id
        AND passenger_address.passenger_id_id = passenger.id
        AND passenger_address.state = station_address.state;
        """ },
    {'query_name': 'Find the top ten trains that has been worked on the most. Return train id and the number of workers that have worked on that train.', 
    'query': """ 
        SELECT train.id as train_id, COUNT (work_roster.personnel_id_id) as number_of_workers
        FROM train, work_roster, personnel
        WHERE train.id = work_roster.train_id_id
        AND work_roster.personnel_id_id = personnel.id
        GROUP BY train.id
        ORDER BY COUNT(work_roster.personnel_id_id) DESC
        LIMIT 10;
        """ },
    {'query_name': 'Find all passengers living in New York City.', 
    'query': """ 
        SELECT Passenger.first_name || ' ' || Passenger.last_name as full_name
        FROM Passenger, passenger_address
        WHERE Passenger.id = passenger_address.passenger_id_id AND passenger_address.city = 'New York City'
        GROUP BY Passenger.id;
        """ },
]

def index(request):
    return render(request, 'dbmsops/index.html', {'db_tables': db_tables})

def reports(request):
    return render(request, 'dbmsops/reports.html', {'members_and_queries': members_and_queries})

# Have to make changes once every member's query is finalized
def report_details(request, report_number):
    res = get_sql_result(members_and_queries[report_number-1]['query'])
    qs = []
    if report_number == 1:
        for tup in res:
            qs.append(Query1Model(passenger_id=tup[0]))
        tb_data = Query1Table(qs)
    elif report_number == 2:
        for tup in res:
            qs.append(Query2Model(first_name=tup[0], last_name=tup[1], amount=tup[2]))
        tb_data = Query2Table(qs)
    elif report_number == 3:
        for tup in res:
            qs.append(Query3Model(full_name=tup[0], no_of_tickets=tup[1]))
        tb_data = Query3Table(qs)
    elif report_number == 4:
        for tup in res:
            qs.append(Query4Model(station_name=tup[0], no_of_trains=tup[1]))
        tb_data = Query4Table(qs)
    elif report_number == 5:
        for tup in res:
            qs.append(Query5Model(no_of_stops=tup[0], trip_id=tup[1]))
        tb_data = Query5Table(qs)
    elif report_number == 6:
        for tup in res:
            qs.append(Query6Model(full_name=tup[0], personnel_id=tup[1]))
        tb_data = Query6Table(qs)
    elif report_number == 6:
        for tup in res:
            qs.append(Query7Model(no_of_passengers=tup[0]))
        tb_data = Query7Table(qs)
    elif report_number == 7:
        for tup in res:
            qs.append(Query7Model(no_of_passengers=tup[0]))
        tb_data = Query7Table(qs)
    elif report_number == 8:
        for tup in res:
            qs.append(Query8Model(passenger_id=tup[0], state=tup[1]))
        tb_data = Query8Table(qs)
    elif report_number == 9:
        for tup in res:
            qs.append(Query9Model(train_id=tup[0], number_of_workers=tup[1]))
        tb_data = Query9Table(qs)
    elif report_number == 10:
        for tup in res:
            qs.append(Query3Model(full_name=tup[0]))
        tb_data = Query10Table(qs)

      # enable sorting
    RequestConfig(request).configure(tb_data)
    tb_data.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'dbmsops/details.html', {'tb_data': tb_data, 'member_and_query': members_and_queries[report_number-1]})

def get_sql_result(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row

def data_entry_form(request, table_name):
    table_name = table_name.strip()
    tb_data = db_tables[table_name][table_name + 'Table'](db_tables[table_name][ table_name + 'Model'].objects.all())
    tb_schema = db_tables[table_name]['tb_name'] + db_tables[table_name]['tb_fields']
    RequestConfig(request).configure(tb_data)
    tb_data.paginate(page=request.GET.get('page', 1), per_page=10)
    error = 'None'
    if request.method == 'POST':
        query_set = request.POST
        error = form_validation_helper(query_set)
        tb_data = db_tables[table_name][table_name +'Table'](db_tables[table_name][table_name + 'Model'].objects.all())
        RequestConfig(request).configure(tb_data)
        tb_data.paginate(page=request.GET.get('page', 1), per_page=10)

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
                    existing_trip = Trip.objects.get(id=query_set['Ticket_tripID'])
                    new_ticket = Ticket(passenger_id=existing_passenger, trip_id=existing_trip, purchase_date=query_set['Ticket_purchaseDate'],
                        expiration_date=query_set['Ticket_expirationDate'], is_valid=query_set['Ticket_isValid'], fare=query_set['Ticket_fare'])
                    try:
                        new_ticket.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Passenger with ID of {passengerID} does not exists or Trip with ID {tripID} does not exists'.format(passengerID=query_set['Ticket_passengerID'], tripID=query_set['Ticket_tripID'])
            elif key.startswith('Stop_stationID'):
                try:
                    existing_station = Station.objects.get(id=query_set['Stop_stationID'])
                    existing_trip = Trip.objects.get(id=query_set['Stop_tripID'])
                    new_stop = Stop(station_id=existing_station,route_index=query_set['Stop_routeIndex'],arrival_time=query_set['Stop_stopArrivalTime'],departure_time=query_set['Stop_stopDepartureTime'],trip_id=existing_trip, date=query_set['Stop_date'])
                    try:
                        new_stop.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Station with ID of {stationID} does not exists or Trip with ID {tripID} does not exists'.format(stationID=query_set['Stop_stationID'], tripID=query_set['Stop_tripID'])
            elif key.startswith('Station_stationName'):
                try:
                    new_station = Station(station_name=query_set['Station_stationName'], built_year=query_set['Station_builtYear'])
                    new_station.save()
                except Exception as err:
                        error = 'Error: ' + err
            elif key.startswith('Trip_trainID'):
                try:
                    existing_train = Train.objects.get(id=query_set['Trip_trainID'])
                    new_trip = Trip(travels_on=existing_train, date=query_set['Trip_date'], distance=query_set['Trip_distance'], duration=query_set['Trip_duration'])
                    try:
                        new_trip.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Train with ID {trainID} does not exists'.format(trainID=query_set['Trip_trainID'])
            elif key.startswith('Train_model'):
                try:
                    new_train = Train(model=query_set['Train_model'], year=query_set['Train_year'], type=query_set['Train_type'])
                    new_train.save()
                except Exception as err:
                    error = 'Error: ' + err
            elif key.startswith('Personnel_firstName'):
                try:
                    new_personnel = Personnel(first_name=query_set['Personnel_firstName'], last_name=query_set['Personnel_lastName'], dob=query_set['Personnel_DOB'])
                    new_personnel.save()
                except Exception as err:
                    error = 'Error: ' + err
            elif key.startswith('PassengerAddress_passengerID'):
                zip_code = query_set['PassengerAddress_zip']
                while len(zip_code) < 5:
                    zip_code = '0' + zip_code 
                try:
                    existing_passenger = Passenger.objects.get(id=query_set['PassengerAddress_passengerID'])
                    try:
                        new_passenger_address = PassengerAddress(passenger_id=existing_passenger, street=query_set['PassengerAddress_street'], country=query_set['PassengerAddress_country'], state=query_set['PassengerAddress_state'], city=query_set['PassengerAddress_city'], zip=zip_code)
                        new_passenger_address.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Passenger with ID {passengerID} does not exists'.format(passengerID=query_set['PassengerAddress_passengerID'])
            elif key.startswith('StationAddress_stationID'):
                zip_code = query_set['StationAddress_zip']
                station_already_exists = False
                station_address_already_exists = False
                while len(zip_code) < 5:
                    zip_code = '0' + zip_code
                print(zip_code)
                try:
                    existing_station = Station.objects.get(id=query_set['StationAddress_stationID'])
                    station_already_exists = True
                    StationAddress.objects.get(station=existing_station)
                    station_address_already_exists = True

                    if station_already_exists == True and station_address_already_exists == True:
                        error = 'Error: Station with {stationID} already has a address and it cannot have multiple addresses'.format(stationID=query_set['StationAddress_stationID'])
                except Exception as err:
                    if station_already_exists == True and station_address_already_exists == False:
                        try:
                            new_station_address = StationAddress(station=existing_station, street=query_set['StationAddress_street'], country=query_set['StationAddress_country'], state=query_set['StationAddress_state'], city=query_set['StationAddress_city'], zip=zip_code)
                            new_station_address.save()
                        except Exception as err:
                            error = 'Error: ' + err
                    elif station_address_already_exists == True:
                        error = 'Error: Station with {stationID} already has a address and it cannot have multiple addresses'.format(stationID=query_set['StationAddress_stationID'])
                    else:
                        error = 'Error: Station with ID {stationID} does not exists'.format(stationID=query_set['StationAddress_stationID'])
            elif key.startswith('WorkRoster_personnelID'):
                try:
                    existing_personnel = Personnel.objects.get(id=query_set['WorkRoster_personnelID'])
                    existing_train = Train.objects.get(id=query_set['WorkRoster_trainID'])
                    try:
                        new_workroster = WorkRoster(personnel_id=existing_personnel, train_id=existing_train, role=query_set['WorkRoster_role'], work_date=query_set['WorkRoster_workDate'])
                        new_workroster.save()
                    except Exception as err:
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Personnel with ID of {personnelID} does not exists or Train with ID {trainID} does not exists'.format(personnelID=query_set['WorkRoster_personnelID'], trainID=query_set['WorkRoster_trainID'])
            elif key.startswith('ScheduledOn_stationID'):
                try:
                    existing_station = Station.objects.get(id=query_set['ScheduledOn_stationID'])
                    existing_trip = Trip.objects.get(id=query_set['ScheduledOn_tripID'])
                    try:
                        new_scheduledon = ScheduledOn(station_id=existing_station, trip_id=existing_trip, date=query_set['ScheduledOn_date'], time=query_set['Scheduled_time'])
                        new_scheduledon.save()
                    except Exception as err: 
                        error = 'Error: ' + err
                except Exception as err:
                    error = 'Error: Station with ID of {stationID} does not exists or Trip with ID {tripID} does not exists'.format(stationID=query_set['ScheduledOn_stationID'], tripID=query_set['ScheduledOn_tripID'])
    return error