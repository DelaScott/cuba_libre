# Generated by Django 4.2.1 on 2023-06-03 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='cars/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('availability_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='guides/')),
                ('description', models.TextField()),
                ('services', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='RentalProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='rental_properties/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('availability_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.car')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.guide')),
                ('rental_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.rentalproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
