# Generated by Django 3.2.8 on 2021-11-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatures', '0003_auto_20211111_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidature',
            name='antiquity_3_years',
            field=models.BooleanField(default=False, verbose_name='Antigüedad > 3 años'),
        ),
    ]