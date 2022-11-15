from django.urls import path
from . import views

app_name = 'dbmsops'
urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('ajax/load-data-entry-form/', views.load_data_entry_form, name='load_data_entry_form'),
]