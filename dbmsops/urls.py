from django.urls import path
from . import views

app_name = 'dbmsops'
urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports')
]