# Generated by Django 4.2.4 on 2023-08-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0007_alter_spieler_deca_alter_spieler_discm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spieler',
            name='punkte',
            field=models.IntegerField(default=0),
        ),
    ]