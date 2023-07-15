from django.urls import path
from .views import property_list, property_detail, booking_list, booking_detail

app_name = 'housing'

urlpatterns = [
    path('properties/', property_list, name='property_list'),
    path('property/<int:pk>/', property_detail, name='property_detail'),
    path('bookings/', booking_list, name='booking_list'),
    path('booking/<int:pk>/', booking_detail, name='booking_detail'),
]
