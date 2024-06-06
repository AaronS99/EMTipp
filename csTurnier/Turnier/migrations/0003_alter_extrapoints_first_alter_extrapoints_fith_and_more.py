# Generated by Django 4.1.7 on 2023-03-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0002_extrapoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrapoints',
            name='first',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='fith',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='fourth',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='second',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='extrapoints',
            name='third',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='games',
            name='playerI',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='games',
            name='playerII',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='games',
            name='winner',
            field=models.CharField(blank=True, choices=[('sanPedro', 'LukasT'), ('Loki', 'LukasL'), ('coolJojo', 'Jojo'), ('mare', 'Marc'), ('awonga', 'Aaron')], default='', max_length=30),
        ),
    ]