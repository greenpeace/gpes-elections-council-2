# Generated by Django 3.2.8 on 2021-11-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatures', '0007_auto_20211119_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidature',
            name='seniority_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha antigüedad'),
        ),
    ]