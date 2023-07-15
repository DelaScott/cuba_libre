from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Property(models.Model):
    ROOMS_CHOICES = [(i, f'{i} room' if i == 1 else f'{i} rooms') for i in range(1, 11)]
    GUESTS_CHOICES = [(i, f'{i} guest' if i == 1 else f'{i} guest') for i in range(1, 11)]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    num_rooms = models.IntegerField(choices=ROOMS_CHOICES)
    num_guests = models.IntegerField(choices=GUESTS_CHOICES)
    phone = models.ManyToManyField('Phone')
    emails = models.ManyToManyField('Email')

    def __str__(self):
        return self.title

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Phone(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. Максимальное количество символов: 15."
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    def __str__(self):
        return self.phone    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.property.title} - {self.booking_date}"


