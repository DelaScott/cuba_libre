# Generated by Django 4.2.1 on 2023-06-12 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("housing", "0008_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="property",
            old_name="num_people",
            new_name="num_guests",
        ),
        migrations.RemoveField(
            model_name="property",
            name="addres_link",
        ),
        migrations.AlterField(
            model_name="property",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=15,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Номер телефона должен быть в формате: '+999999999'. Максимальное количество символов: 15.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
    ]