from base import pvesti, volgograd, oktavito, riac34, youla
from django.urls import  path
from main.views import ListOktMainView, ImportView, FileImportView
from main.api.views import generate_years


urlpatterns = [
    path('', ListOktMainView.as_view(), name='main'),
    path('prefimport/', ImportView.as_view(), name='foto-admin'),
    path('fileimport/', FileImportView.as_view(), name='file-admin'),
    path('pvesti_parser/', pvesti.PvestiView.as_view(), name='pvesti_parser'),
    path('volgograd_parser/', volgograd.VolgogradView.as_view(), name='volgograd_parser'),
    path('oktavito_parser/', oktavito.AvitoView.as_view(), name='oktavito_parser'),
    path('riac34_parser/', riac34.Rica34View.as_view(), name='riac34_parser'),
    path('youla_parser/', youla.YoulaView.as_view(), name='youla_parser'),
    path('<int:id>/', generate_years, name='generate_years')

]

