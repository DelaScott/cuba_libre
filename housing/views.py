from django.shortcuts import render
from .models import Property, Booking


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'housing/property_list.html', {'properties': properties})


def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'housing/property_detail.html', {'property': property})


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'housing/booking_list.html', {'bookings': bookings})


def booking_detail(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'housing/booking_detail.html', {'booking': booking})
