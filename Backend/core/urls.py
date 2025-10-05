# core/urls.py

from django.urls import path
from .views import ClimaListAllView, ClimaListByCityView, ClimaDetailByCityDayView

urlpatterns = [
    # URL para obtener todos los datos
    path('api/clima/all/', ClimaListAllView.as_view(), name='clima-list-all'),

    # URL para obtener datos por ciudad
    path('api/clima/<str:ciudad>/', ClimaListByCityView.as_view(), name='clima-list-by-city'),

    # URL para obtener datos por ciudad y día
    path('api/clima/<str:ciudad>/<int:dia>/', ClimaDetailByCityDayView.as_view(), name='clima-detail-by-city-day'),
]