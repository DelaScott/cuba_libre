from django.db import models

# Create your models here.
class Guide(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='guides/')
    description = models.TextField()
    services = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name