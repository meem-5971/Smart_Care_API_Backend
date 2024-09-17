# Generated by Django 5.0.4 on 2024-09-16 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('doctor', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
