# Generated by Django 4.2.4 on 2023-08-18 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0013_results_xdeca_results_xdiscm_results_xdiscw_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spieler',
            name='punkte',
        ),
    ]