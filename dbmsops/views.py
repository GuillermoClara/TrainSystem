from django.shortcuts import render

def index(request):
    return render(request, 'dbmsops/index.html')

def reports(request):
    return render(request, 'dbmsops/reports.html')