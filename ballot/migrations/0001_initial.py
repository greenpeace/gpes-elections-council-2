# Generated by Django 3.2.8 on 2022-01-07 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circumscription', '0002_auto_20211104_1505'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_date', models.DateTimeField(null=True, verbose_name='Fecha de votación')),
                ('blank_vote', models.BooleanField(verbose_name='Voto en blanco')),
                ('null_vote', models.BooleanField(verbose_name='Voto nulo')),
                ('circumscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ballot_circumscription_set', to='circumscription.circumscription', verbose_name='Circunscripción')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ballot_user_set', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Papeleta',
                'verbose_name_plural': 'Papeletas',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_ballot_set', to='ballot.ballot')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_candidate_set', to='circumscription.circumscription')),
            ],
            options={
                'verbose_name': 'Voto',
                'verbose_name_plural': 'Votos',
            },
        ),
    ]
