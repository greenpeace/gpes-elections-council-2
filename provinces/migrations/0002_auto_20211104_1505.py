# Generated by Django 3.2.8 on 2021-11-04 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circumscription', '0002_auto_20211104_1505'),
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='district',
        ),
        migrations.AddField(
            model_name='province',
            name='circumscription',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='province_circumscription_set', to='circumscription.circumscription'),
            preserve_default=False,
        ),
    ]
