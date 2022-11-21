from django.shortcuts import render
from dbmsops.models import Passenger 
from .tables import PassengerTable, PassengerTable2

db_tables = {
    "1": {"tb_name": "Passenger", "tb_fields":"(PassengerID, lastName, firstName)"},
    "2": {"tb_name": "Route",  "tb_fields":"(RouteID, Source, destination)"},
    "3": {"tb_name": "Stops","tb_fields":"(stationName, StationID, positionsOfOrder)"},
    "4": {"tb_name": "Station","tb_fields":"(RouteID, Source, destination)"},
    "5": {"tb_name": "Trip","tb_fields":"(tripID,depatureTime, arrivalTime, date)"},
    "6": {"tb_name": "Train","tb_fields":"(trainID,model,year)"},
    "7": {"tb_name": "Personnel","tb_fields":"(DoB, lastname, firstName, personellD)"}
}

members_and_queries = [
    {'member_name': 'Mr. A', 'query': 'SELECT id, first_name FROM passenger'},
    {'member_name': 'Mr. B', 'query': 'SELECT id, first_name FROM passenger'}
]

def index(request):
    # print(Passenger.objects.all())
    table = PassengerTable(Passenger.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=2)
    if request.method == 'POST':
        print(request.POST['passengerID'])
        print(request.POST['firstName'])
        print(request.POST['lastName'])
    return render(request, 'dbmsops/index.html', {'db_tables': db_tables, 'passenger_tb_rows':table})

def reports(request):
    return render(request, 'dbmsops/reports.html', {'members_and_queries': members_and_queries})

def details(request, report_number):
    print(report_number)
    tb_data = PassengerTable2(Passenger.objects.raw(members_and_queries[report_number-1]['query']))
    tb_data.paginate(page=request.GET.get("page", 1), per_page=2)
    return render(request, 'dbmsops/details.html', {'tb_data': tb_data, 'member_and_query': members_and_queries[report_number-1]})

def load_data_entry_form(request):
    tb_option = request.GET.get('tb_option')
    template = 'dbmsops/forms/' + db_tables[tb_option]['tb_name'].lower() + '_form.html'
    return render(request, template, {'tb_schema': db_tables[tb_option]['tb_name'] + db_tables[tb_option]['tb_fields']})