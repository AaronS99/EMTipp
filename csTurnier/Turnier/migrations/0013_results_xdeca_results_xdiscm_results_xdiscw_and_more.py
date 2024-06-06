# Generated by Django 4.2.4 on 2023-08-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnier', '0012_alter_spieler_deca_alter_spieler_discm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='xdeca',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xdiscM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xdiscW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xeightM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xeightW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfifteenM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfifteenW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfiveKM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfiveKW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourHM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourHW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourxfourM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourxfourW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourxoneM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xfourxoneW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhammerM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhammerW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhepta',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhighM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhighW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhundredM',
            field=models.CharField(blank=True, default='tbd', max_length=40, verbose_name='100m Männer'),
        ),
        migrations.AddField(
            model_name='results',
            name='xhundredW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhurdlesM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xhurdlesW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xjavM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xjavW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xlongM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xlongW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xpoleVM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xpoleVW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xshotM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xshotW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xsteepleM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xsteepleW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtenKM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtenKW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtripleM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtripleW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtwoM',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
        migrations.AddField(
            model_name='results',
            name='xtwoW',
            field=models.CharField(blank=True, default='tbd', max_length=40),
        ),
    ]