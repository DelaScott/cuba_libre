from django.urls import path
from .views import car_list, car_detail

app_name = 'car_rental'

urlpatterns = [
    path('', car_list, name='car_list'),
    path('<int:pk>/', car_detail, name='car_detail'),
]
