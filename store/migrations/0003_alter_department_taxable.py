# Generated by Django 4.2 on 2023-05-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_device_devicedefect_workordercart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='taxable',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3),
        ),
    ]
