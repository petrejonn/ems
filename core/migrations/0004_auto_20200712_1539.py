# Generated by Django 3.0.8 on 2020-07-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200711_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedepartment',
            name='date_left',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='employeeposition',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
