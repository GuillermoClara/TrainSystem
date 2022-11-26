from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dbmsops.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'dbmsops.views.not_found_404_view'
handler500 = 'dbmsops.views.server_error_500_view'