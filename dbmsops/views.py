from django.shortcuts import render

db_tables = {
    "1": {"tb_name": "Passenger", "tb_schema":"(PassengerID, lastName, firstName)"},
    "2": {"tb_name": "Route",  "tb_schema":"(RouteID, Source, destination)"},
    "3": {"tb_name": "Stops","tb_schema":"(stationName, StationID, positionsOfOrder)"},
    "4": {"tb_name": "Station","tb_schema":"(RouteID, Source, destination)"},
    "5": {"tb_name": "Trip","tb_schema":"(tripID,depatureTime, arrivalTime, date)"},
    "6": {"tb_name": "Train","tb_schema":"(trainID,model,year)"},
    "7": {"tb_name": "Personnel","tb_schema":"(DoB, lastname, firstName, personellD)"}
}

def index(request):
    return render(request, 'dbmsops/index.html', {'db_tables': db_tables})

def reports(request):
    return render(request, 'dbmsops/reports.html')

def load_data_entry_form(request):
    dboption_id = request.GET.get('dboption')
    templatePath = 'dbmsops/forms/' + db_tables[dboption_id]['tb_name'].lower() + '_form.html'
    return render(request, templatePath)