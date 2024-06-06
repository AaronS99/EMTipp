from django.db import models

# Create your models here.
playerList = [
    ("sanPedro", "LukasT"),
    ("Loki", "LukasL"),
    ("coolJojo", "Jojo"),
    ("mare", "Marc"),
    ("awonga", "Aaron")
]

class Players(models.Model):
    name = models.CharField(max_length=200, default='')
    nickname = models.CharField(max_length=200, default='')
    age = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name}'

class Games(models.Model):
    playerI = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    playerII = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    finished = models.BooleanField(default=False)
    score = models.CharField(max_length=10, default='0:0')
    winner = models.CharField(max_length=30, choices=playerList, default="", blank=True)

    def __str__(self):
        return f'{self.playerI}{self.playerII}'

class extraPoints(models.Model):
    first = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    second = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    third = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    fourth = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    fith = models.CharField(max_length=30, choices=playerList, default="", blank=True)
    firstPoints = models.IntegerField(default=0, blank = True)
    secondPoints = models.IntegerField(default=0, blank = True)
    thirdPoints = models.IntegerField(default=0, blank = True)
    fourthPoints = models.IntegerField(default=0, blank = True)
    fifthPoints = models.IntegerField(default=0, blank = True)

    def __str__(self):
        return f'{self.first}'


class Event(models.Model):
    name = models.CharField(max_length=40, default="")
    date = models.CharField(max_length=40, default="")
    time = models.CharField(max_length=40, default="")
    first = models.CharField(max_length=40, default="")
    second = models.CharField(max_length=40, default="")
    third = models.CharField(max_length=40, default="")
    def __str__(self):
        return f'{self.name}'

class Spieler(models.Model):
    name = models.CharField(max_length=40, default="")
    hundredM = models.CharField(verbose_name="100m Männer", max_length=40, default="", blank=True)
    hundredW= models.CharField(verbose_name="100m Frauen", max_length=40, default="", blank=True)
    hurdlesM = models.CharField(verbose_name="110m Hürden Männer", max_length=40, default="", blank=True)
    hurdlesW = models.CharField(verbose_name="100m Hürden Frauen", max_length=40, default="", blank=True)
    twoM = models.CharField(verbose_name="200m Männer", max_length=40, default="", blank=True)
    twoW = models.CharField(verbose_name="200m Frauen", max_length=40, default="", blank=True)
    deca = models.CharField(verbose_name="Zehnkampf", max_length=40, default="", blank=True)
    hepta = models.CharField(verbose_name="Siebenkampf", max_length=40, default="", blank=True)
    fourM = models.CharField(verbose_name="400m Männer", max_length=40, default="", blank=True)
    fourW = models.CharField(verbose_name="400m Frauen", max_length=40, default="", blank=True)
    fourHM = models.CharField(verbose_name="400m Hürden Männer", max_length=40, default="", blank=True)
    fourHW = models.CharField(verbose_name="400m Hürden Frauen", max_length=40, default="", blank=True)
    eightM = models.CharField(verbose_name="800m Männer", max_length=40, default="", blank=True)
    eightW = models.CharField(verbose_name="800m Frauen", max_length=40, default="", blank=True)
    fifteenM = models.CharField(verbose_name="1500m Männer", max_length=40, default="", blank=True)
    fifteenW = models.CharField(verbose_name="1500m Frauen", max_length=40, default="", blank=True)
    fiveKM = models.CharField(verbose_name="5km Männer", max_length=40, default="", blank=True)
    fiveKW = models.CharField(verbose_name="5km Frauen", max_length=40, default="", blank=True)
    tenKM = models.CharField(verbose_name="10km Männer", max_length=40, default="", blank=True)
    tenKW = models.CharField(verbose_name="10km Frauen", max_length=40, default="", blank=True)
    steepleM = models.CharField(verbose_name="3000m Hindernis Männer", max_length=40, default="", blank=True)
    steepleW = models.CharField(verbose_name="3000m Hindernis Frauen", max_length=40, default="", blank=True)
    highM = models.CharField(verbose_name="Hochsprung Männer", max_length=40, default="", blank=True)
    highW = models.CharField(verbose_name="Hochsprung Frauen", max_length=40, default="", blank=True)
    poleVM = models.CharField(verbose_name="Stabhochsprung Männer", max_length=40, default="", blank=True)
    poleVW = models.CharField(verbose_name="Stabhochsprung Frauen", max_length=40, default="", blank=True)
    longM = models.CharField(verbose_name="Weitsprung Männer", max_length=40, default="", blank=True)
    longW = models.CharField(verbose_name="Weitsprung Frauen", max_length=40, default="", blank=True)
    tripleM = models.CharField(verbose_name="Dreisprung Männer", max_length=40, default="", blank=True)
    tripleW = models.CharField(verbose_name="Dreisprung Frauen", max_length=40, default="", blank=True)
    shotM = models.CharField(verbose_name="Kugelstoß Männer", max_length=40, default="", blank=True)
    shotW = models.CharField(verbose_name="Kugelstoß Frauen", max_length=40, default="", blank=True)
    discM = models.CharField(verbose_name="Diskuswurf Männer", max_length=40, default="", blank=True)
    discW = models.CharField(verbose_name="Diskuswurf Frauen", max_length=40, default="", blank=True)
    hammerM = models.CharField(verbose_name="Hammerwurf Männer", max_length=40, default="", blank=True)
    hammerW = models.CharField(verbose_name="Hammerwurf Frauen", max_length=40, default="", blank=True)
    javM = models.CharField(verbose_name="Speerwurf Männer", max_length=40, default="", blank=True)
    javW = models.CharField(verbose_name="Speerwurf Frauen", max_length=40, default="", blank=True)
    fourxoneM = models.CharField(verbose_name="4x100m Männer", max_length=40, default="", blank=True)
    fourxoneW = models.CharField(verbose_name="4x100m Frauen", max_length=40, default="", blank=True)
    fourxfourM = models.CharField(verbose_name="4x400m Männer", max_length=40, default="", blank=True)
    fourxfourW = models.CharField(verbose_name="4x400m Frauen", max_length=40, default="", blank=True)
    fourxfourX = models.CharField(verbose_name="4x400m Mixed", max_length=40, default="", blank=True)
    def __str__(self):
        return f'{self.name}'


class Results(models.Model):
    rank = models.CharField(max_length=5, default="")
    value = models.IntegerField(default=0)
    hundredM = models.CharField(verbose_name="100m Männer", max_length=40, default="tbd", blank=True)
    hundredW= models.CharField(max_length=40, default="tbd", blank=True)
    hurdlesM = models.CharField(max_length=40, default="tbd", blank=True)
    hurdlesW = models.CharField(max_length=40, default="tbd", blank=True)
    twoM = models.CharField(max_length=40, default="tbd", blank=True)
    twoW = models.CharField(max_length=40, default="tbd", blank=True)
    deca = models.CharField(max_length=40, default="tbd", blank=True)
    hepta = models.CharField(max_length=40, default="tbd", blank=True)
    fourM = models.CharField(max_length=40, default="tbd", blank=True)
    fourW = models.CharField(max_length=40, default="tbd", blank=True)
    fourHM = models.CharField(max_length=40, default="tbd", blank=True)
    fourHW = models.CharField(max_length=40, default="tbd", blank=True)
    eightM = models.CharField(max_length=40, default="tbd", blank=True)
    eightW = models.CharField(max_length=40, default="tbd", blank=True)
    fifteenM = models.CharField(max_length=40, default="tbd", blank=True)
    fifteenW = models.CharField(max_length=40, default="tbd", blank=True)
    fiveKM = models.CharField(max_length=40, default="tbd", blank=True)
    fiveKW = models.CharField(max_length=40, default="tbd", blank=True)
    tenKM = models.CharField(max_length=40, default="tbd", blank=True)
    tenKW = models.CharField(max_length=40, default="tbd", blank=True)
    steepleM = models.CharField(max_length=40, default="tbd", blank=True)
    steepleW = models.CharField(max_length=40, default="tbd", blank=True)
    highM = models.CharField(max_length=40, default="tbd", blank=True)
    highW = models.CharField(max_length=40, default="tbd", blank=True)
    poleVM = models.CharField(max_length=40, default="tbd", blank=True)
    poleVW = models.CharField(max_length=40, default="tbd", blank=True)
    longM = models.CharField(max_length=40, default="tbd", blank=True)
    longW = models.CharField(max_length=40, default="tbd", blank=True)
    tripleM = models.CharField(max_length=40, default="tbd", blank=True)
    tripleW = models.CharField(max_length=40, default="tbd", blank=True)
    shotM = models.CharField(max_length=40, default="tbd", blank=True)
    shotW = models.CharField(max_length=40, default="tbd", blank=True)
    discM = models.CharField(max_length=40, default="tbd", blank=True)
    discW = models.CharField(max_length=40, default="tbd", blank=True)
    hammerM = models.CharField(max_length=40, default="tbd", blank=True)
    hammerW = models.CharField(max_length=40, default="tbd", blank=True)
    javM = models.CharField(max_length=40, default="tbd", blank=True)
    javW = models.CharField(max_length=40, default="tbd", blank=True)
    fourxoneM = models.CharField(max_length=40, default="tbd", blank=True)
    fourxoneW = models.CharField(max_length=40, default="tbd", blank=True)
    fourxfourM = models.CharField(max_length=40, default="tbd", blank=True)
    fourxfourW = models.CharField(max_length=40, default="tbd", blank=True)
    fourxfourX = models.CharField(max_length=40, default="", blank=True)


    xhundredM = models.CharField(verbose_name="100m Männer", max_length=40, default="tbd", blank=True)
    xhundredW= models.CharField(max_length=40, default="tbd", blank=True)
    xhurdlesM = models.CharField(max_length=40, default="tbd", blank=True)
    xhurdlesW = models.CharField(max_length=40, default="tbd", blank=True)
    xtwoM = models.CharField(max_length=40, default="tbd", blank=True)
    xtwoW = models.CharField(max_length=40, default="tbd", blank=True)
    xdeca = models.CharField(max_length=40, default="tbd", blank=True)
    xhepta = models.CharField(max_length=40, default="tbd", blank=True)
    xfourM = models.CharField(max_length=40, default="tbd", blank=True)
    xfourW = models.CharField(max_length=40, default="tbd", blank=True)
    xfourHM = models.CharField(max_length=40, default="tbd", blank=True)
    xfourHW = models.CharField(max_length=40, default="tbd", blank=True)
    xeightM = models.CharField(max_length=40, default="tbd", blank=True)
    xeightW = models.CharField(max_length=40, default="tbd", blank=True)
    xfifteenM = models.CharField(max_length=40, default="tbd", blank=True)
    xfifteenW = models.CharField(max_length=40, default="tbd", blank=True)
    xfiveKM = models.CharField(max_length=40, default="tbd", blank=True)
    xfiveKW = models.CharField(max_length=40, default="tbd", blank=True)
    xtenKM = models.CharField(max_length=40, default="tbd", blank=True)
    xtenKW = models.CharField(max_length=40, default="tbd", blank=True)
    xsteepleM = models.CharField(max_length=40, default="tbd", blank=True)
    xsteepleW = models.CharField(max_length=40, default="tbd", blank=True)
    xhighM = models.CharField(max_length=40, default="tbd", blank=True)
    xhighW = models.CharField(max_length=40, default="tbd", blank=True)
    xpoleVM = models.CharField(max_length=40, default="tbd", blank=True)
    xpoleVW = models.CharField(max_length=40, default="tbd", blank=True)
    xlongM = models.CharField(max_length=40, default="tbd", blank=True)
    xlongW = models.CharField(max_length=40, default="tbd", blank=True)
    xtripleM = models.CharField(max_length=40, default="tbd", blank=True)
    xtripleW = models.CharField(max_length=40, default="tbd", blank=True)
    xshotM = models.CharField(max_length=40, default="tbd", blank=True)
    xshotW = models.CharField(max_length=40, default="tbd", blank=True)
    xdiscM = models.CharField(max_length=40, default="tbd", blank=True)
    xdiscW = models.CharField(max_length=40, default="tbd", blank=True)
    xhammerM = models.CharField(max_length=40, default="tbd", blank=True)
    xhammerW = models.CharField(max_length=40, default="tbd", blank=True)
    xjavM = models.CharField(max_length=40, default="tbd", blank=True)
    xjavW = models.CharField(max_length=40, default="tbd", blank=True)
    xfourxoneM = models.CharField(max_length=40, default="tbd", blank=True)
    xfourxoneW = models.CharField(max_length=40, default="tbd", blank=True)
    xfourxfourM = models.CharField(max_length=40, default="tbd", blank=True)
    xfourxfourW = models.CharField(max_length=40, default="tbd", blank=True)
    xfourxfourX = models.CharField(max_length=40, default="", blank=True)

    def __str__(self):
        return f'{self.rank}'