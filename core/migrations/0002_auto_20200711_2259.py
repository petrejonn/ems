# Generated by Django 3.0.8 on 2020-07-11 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='retirment_date',
            new_name='retirement_date',
        ),
    ]
