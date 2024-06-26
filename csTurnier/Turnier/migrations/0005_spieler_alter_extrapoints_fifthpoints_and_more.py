# Generated by Django 4.2.4 on 2023-08-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0004_extrapoints_fifthpoints_extrapoints_firstpoints_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spieler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('hundredM', models.CharField(default='', max_length=40)),
                ('hundredW', models.CharField(default='', max_length=40)),
                ('hurdlesM', models.CharField(default='', max_length=40)),
                ('hurdlesW', models.CharField(default='', max_length=40)),
                ('twoM', models.CharField(default='', max_length=40)),
                ('twoW', models.CharField(default='', max_length=40)),
                ('deca', models.CharField(default='', max_length=40)),
                ('hepta', models.CharField(default='', max_length=40)),
                ('fourM', models.CharField(default='', max_length=40)),
                ('fourW', models.CharField(default='', max_length=40)),
                ('fourHM', models.CharField(default='', max_length=40)),
                ('fourHW', models.CharField(default='', max_length=40)),
                ('eightM', models.CharField(default='', max_length=40)),
                ('eightW', models.CharField(default='', max_length=40)),
                ('fifteenM', models.CharField(default='', max_length=40)),
                ('fifteenW', models.CharField(default='', max_length=40)),
                ('fiveKM', models.CharField(default='', max_length=40)),
                ('fiveKW', models.CharField(default='', max_length=40)),
                ('tenKM', models.CharField(default='', max_length=40)),
                ('tenKW', models.CharField(default='', max_length=40)),
                ('steepleM', models.CharField(default='', max_length=40)),
                ('steepleW', models.CharField(default='', max_length=40)),
                ('highM', models.CharField(default='', max_length=40)),
                ('highW', models.CharField(default='', max_length=40)),
                ('poleVM', models.CharField(default='', max_length=40)),
                ('poleVW', models.CharField(default='', max_length=40)),
                ('longM', models.CharField(default='', max_length=40)),
                ('longW', models.CharField(default='', max_length=40)),
                ('tripleM', models.CharField(default='', max_length=40)),
                ('tripleW', models.CharField(default='', max_length=40)),
                ('shotM', models.CharField(default='', max_length=40)),
                ('shotW', models.CharField(default='', max_length=40)),
                ('discM', models.CharField(default='', max_length=40)),
                ('discW', models.CharField(default='', max_length=40)),
                ('hammerM', models.CharField(default='', max_length=40)),
                ('hammerW', models.CharField(default='', max_length=40)),
                ('javM', models.CharField(default='', max_length=40)),
                ('javW', models.CharField(default='', max_length=40)),
                ('fourxoneM', models.CharField(default='', max_length=40)),
                ('fourxoneW', models.CharField(default='', max_length=40)),
                ('fourxfourM', models.CharField(default='', max_length=40)),
                ('fourxfourW', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='fifthPoints',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='firstPoints',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='fourthPoints',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='secondPoints',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='thirdPoints',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
