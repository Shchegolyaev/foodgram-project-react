# Generated by Django 3.2.11 on 2022-01-31 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='units',
            new_name='measurement_unit',
        ),
    ]
