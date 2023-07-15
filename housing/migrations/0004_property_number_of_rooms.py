# Generated by Django 4.2.1 on 2023-06-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("housing", "0003_booking_property_delete_rentalproperty_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="number_of_rooms",
            field=models.IntegerField(
                choices=[
                    (1, "1 комната"),
                    (2, "2 комната"),
                    (3, "3 комната"),
                    (4, "4 комната"),
                    (5, "5 комната"),
                    (6, "6 комната"),
                    (7, "7 комната"),
                    (8, "8 комната"),
                    (9, "9 комната"),
                    (10, "10 комната"),
                ],
                default=1,
            ),
            preserve_default=False,
        ),
    ]