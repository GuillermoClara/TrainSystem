from django.urls import path
from . import views

app_name = 'dbmsops'
urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('reports/details/<int:report_number>', views.report_details, name='report_details'),
    path('table/<str:table_name>', views.data_entry_form, name='data_entry_form'),
]
