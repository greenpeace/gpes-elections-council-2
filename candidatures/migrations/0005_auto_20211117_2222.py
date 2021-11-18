# Generated by Django 3.2.8 on 2021-11-17 22:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('council_member', '0002_auto_20211104_1505'),
        ('candidatures', '0004_alter_candidature_antiquity_3_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidature',
            name='presents_it_dni',
            field=models.FileField(null=True, upload_to='%Y/%m/%d', verbose_name='Miembro del Consejo que presenta al candidato/a: Copia del DNI/ Pasaporte/ Tarjeta de residente'),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='campaign',
            field=models.TextField(blank=True, max_length=1000, validators=[django.core.validators.MaxLengthValidator(1000)], verbose_name='¿Qué cambios te gustaría ver en Greenpeace en los próximos tres años? -máximo 1.000 caracteres'),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='presents_it',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidature_council_member_set', to='council_member.councilmember', verbose_name='¿Quien lo presenta?'),
        ),
    ]
