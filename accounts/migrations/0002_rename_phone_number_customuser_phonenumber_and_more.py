# Generated by Django 4.2 on 2023-05-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='service_provider',
            new_name='serviceProvider',
        ),
    ]