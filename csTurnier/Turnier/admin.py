from django.contrib import admin
from .models import Players, Games, extraPoints, Spieler, Results, Event

admin.site.register(Players)
admin.site.register(Games)
admin.site.register(extraPoints)
admin.site.register(Spieler)
admin.site.register(Results)
admin.site.register(Event)

# Register your models here.
