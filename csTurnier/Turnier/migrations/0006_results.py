# Generated by Django 4.2.4 on 2023-08-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0005_spieler_alter_extrapoints_fifthpoints_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='', max_length=5)),
                ('hundredM', models.CharField(blank=True, default='', max_length=40)),
                ('hundredW', models.CharField(blank=True, default='', max_length=40)),
                ('hurdlesM', models.CharField(blank=True, default='', max_length=40)),
                ('hurdlesW', models.CharField(blank=True, default='', max_length=40)),
                ('twoM', models.CharField(blank=True, default='', max_length=40)),
                ('twoW', models.CharField(blank=True, default='', max_length=40)),
                ('deca', models.CharField(blank=True, default='', max_length=40)),
                ('hepta', models.CharField(blank=True, default='', max_length=40)),
                ('fourM', models.CharField(blank=True, default='', max_length=40)),
                ('fourW', models.CharField(blank=True, default='', max_length=40)),
                ('fourHM', models.CharField(blank=True, default='', max_length=40)),
                ('fourHW', models.CharField(blank=True, default='', max_length=40)),
                ('eightM', models.CharField(blank=True, default='', max_length=40)),
                ('eightW', models.CharField(blank=True, default='', max_length=40)),
                ('fifteenM', models.CharField(blank=True, default='', max_length=40)),
                ('fifteenW', models.CharField(blank=True, default='', max_length=40)),
                ('fiveKM', models.CharField(blank=True, default='', max_length=40)),
                ('fiveKW', models.CharField(blank=True, default='', max_length=40)),
                ('tenKM', models.CharField(blank=True, default='', max_length=40)),
                ('tenKW', models.CharField(blank=True, default='', max_length=40)),
                ('steepleM', models.CharField(blank=True, default='', max_length=40)),
                ('steepleW', models.CharField(blank=True, default='', max_length=40)),
                ('highM', models.CharField(blank=True, default='', max_length=40)),
                ('highW', models.CharField(blank=True, default='', max_length=40)),
                ('poleVM', models.CharField(blank=True, default='', max_length=40)),
                ('poleVW', models.CharField(blank=True, default='', max_length=40)),
                ('longM', models.CharField(blank=True, default='', max_length=40)),
                ('longW', models.CharField(blank=True, default='', max_length=40)),
                ('tripleM', models.CharField(blank=True, default='', max_length=40)),
                ('tripleW', models.CharField(blank=True, default='', max_length=40)),
                ('shotM', models.CharField(blank=True, default='', max_length=40)),
                ('shotW', models.CharField(blank=True, default='', max_length=40)),
                ('discM', models.CharField(blank=True, default='', max_length=40)),
                ('discW', models.CharField(blank=True, default='', max_length=40)),
                ('hammerM', models.CharField(blank=True, default='', max_length=40)),
                ('hammerW', models.CharField(blank=True, default='', max_length=40)),
                ('javM', models.CharField(blank=True, default='', max_length=40)),
                ('javW', models.CharField(blank=True, default='', max_length=40)),
                ('fourxoneM', models.CharField(blank=True, default='', max_length=40)),
                ('fourxoneW', models.CharField(blank=True, default='', max_length=40)),
                ('fourxfourM', models.CharField(blank=True, default='', max_length=40)),
                ('fourxfourW', models.CharField(blank=True, default='', max_length=40)),
            ],
        ),
    ]
