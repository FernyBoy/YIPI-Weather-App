from django.shortcuts import render

# core/views.py
from rest_framework.generics import ListAPIView
from .models import Clima
from .serializers import ClimaSerializer

# Vista para obtener TODOS los datos
class ClimaListAllView(ListAPIView):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer

# Vista para obtener datos por CIUDAD
class ClimaListByCityView(ListAPIView):
    serializer_class = ClimaSerializer

    def get_queryset(self):
        ciudad = self.kwargs['ciudad']
        return Clima.objects.filter(ciudad__iexact=ciudad)

# Vista para obtener datos por CIUDAD y DÍA
class ClimaDetailByCityDayView(ListAPIView):
    serializer_class = ClimaSerializer

    def get_queryset(self):
        ciudad = self.kwargs['ciudad']
        dia = self.kwargs['dia']
        return Clima.objects.filter(ciudad__iexact=ciudad, dia=dia)