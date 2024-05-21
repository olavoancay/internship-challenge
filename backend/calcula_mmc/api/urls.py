from django.urls import path
from .views import calcula_mmc_intervalo_api

urlpatterns = [
    path('calcula-mmc-intervalo/', calcula_mmc_intervalo_api, name='calcula_mmc_intervalo_api')
]