# Generated by Django 4.1.7 on 2023-03-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerI', models.CharField(blank=True, choices=[('LT', 'LukasT'), ('LL', 'LukasL'), ('J', 'Jojo'), ('M', 'Marc'), ('A', 'Aaron')], default='', max_length=30)),
                ('playerII', models.CharField(blank=True, choices=[('LT', 'LukasT'), ('LL', 'LukasL'), ('J', 'Jojo'), ('M', 'Marc'), ('A', 'Aaron')], default='', max_length=30)),
                ('finished', models.BooleanField(default=False)),
                ('score', models.CharField(default='0:0', max_length=10)),
                ('winner', models.CharField(blank=True, choices=[('LT', 'LukasT'), ('LL', 'LukasL'), ('J', 'Jojo'), ('M', 'Marc'), ('A', 'Aaron')], default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('nickname', models.CharField(default='', max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
