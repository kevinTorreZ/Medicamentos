from django.contrib import admin
from django.urls import path
from Principal.views import index,productos,cuenta,registrado



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('productos/',productos),
    path('cuenta/',cuenta),
    path('registrado/',registrado)

]
