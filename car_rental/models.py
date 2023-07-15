from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability_date = models.DateField()

    def __str__(self):
        return self.brand
