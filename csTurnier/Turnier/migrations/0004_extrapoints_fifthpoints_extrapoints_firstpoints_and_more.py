# Generated by Django 4.1.7 on 2023-03-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0003_alter_extrapoints_first_alter_extrapoints_fith_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrapoints',
            name='fifthPoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extrapoints',
            name='firstPoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extrapoints',
            name='fourthPoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extrapoints',
            name='secondPoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='extrapoints',
            name='thirdPoints',
            field=models.IntegerField(default=0),
        ),
    ]
