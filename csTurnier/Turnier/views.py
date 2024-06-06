from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Players, Games, extraPoints, Spieler, Results

# Create your views here.


class SpielerCreateView(CreateView):
    model = Spieler
    fields = '__all__'
    success_url = '/Turnier/Overview/'
class SpielerListView(ListView):
    model = Spieler
class SpielerUpdateView(UpdateView):
    model = Spieler
    fields = '__all__'
    success_url = '/Turnier/Overview/'


def Home(request):
    """View function for home page of site."""
    spieler = Spieler.objects.all()
    results = Results.objects.all()
    string = ""

    for spielr in spieler:
        string = string + spielr.name + ": "
        punkte = 0
        for result in results:
            if result.hundredM == spielr.hundredM:
                punkte = punkte + result.value
            
            if result.hundredW == spielr.hundredW:
                punkte = punkte + result.value

            if result.hurdlesM == spielr.hurdlesM:
                punkte = punkte + result.value
            
            if result.hurdlesW == spielr.hurdlesW:
                punkte = punkte + result.value
            
            if result.twoM == spielr.twoM:
                punkte = punkte + result.value
            
            if result.twoW == spielr.twoW:
                punkte = punkte + result.value
            
            if result.deca == spielr.deca:
                punkte = punkte + result.value
            
            if result.hepta == spielr.hepta:
                punkte = punkte + result.value
            
            if result.fourM == spielr.fourM:
                punkte = punkte + result.value
            
            if result.fourW == spielr.fourW:
                punkte = punkte + result.value
            
            if result.fourHM == spielr.fourHM:
                punkte = punkte + result.value
            
            if result.fourHW == spielr.fourHW:
                punkte = punkte + result.value
            
            if result.eightM == spielr.eightM:
                punkte = punkte + result.value
            
            if result.eightW == spielr.eightW:
                punkte = punkte + result.value
            
            if result.fifteenM == spielr.fifteenM:
                punkte = punkte + result.value
            
            if result.fifteenW == spielr.fifteenW:
                punkte = punkte + result.value
            
            if result.fiveKM == spielr.fiveKM:
                punkte = punkte + result.value
            
            if result.fiveKW == spielr.fiveKW:
                punkte = punkte + result.value
            
            if result.tenKM == spielr.tenKM:
                punkte = punkte + result.value
            
            if result.tenKW == spielr.tenKW:
                punkte = punkte + result.value
            
            if result.steepleM == spielr.steepleM:
                punkte = punkte + result.value
            
            if result.steepleW == spielr.steepleW:
                punkte = punkte + result.value
            
            if result.highM == spielr.highM:
                punkte = punkte + result.value
            
            if result.highW == spielr.highW:
                punkte = punkte + result.value

            if result.poleVM == spielr.poleVM:
                punkte = punkte + result.value
            
            if result.poleVW == spielr.poleVW:
                punkte = punkte + result.value

            if result.longM == spielr.longM:
                punkte = punkte + result.value
            
            if result.longW == spielr.longW:
                punkte = punkte + result.value

            if result.tripleM == spielr.tripleM:
                punkte = punkte + result.value
            
            if result.tripleW == spielr.tripleW:
                punkte = punkte + result.value

            if result.shotM == spielr.shotM:
                punkte = punkte + result.value
            
            if result.shotW == spielr.shotW:
                punkte = punkte + result.value

            if result.discM == spielr.discM:
                punkte = punkte + result.value
            
            if result.discW == spielr.discW:
                punkte = punkte + result.value
            
            if result.hammerM == spielr.hammerM:
                punkte = punkte + result.value
            
            if result.hammerW == spielr.hammerW:
                punkte = punkte + result.value
            
            if result.javM == spielr.javM:
                punkte = punkte + result.value
            
            if result.javW == spielr.javW:
                punkte = punkte + result.value
            
            if result.fourxoneM == spielr.fourxoneM:
                punkte = punkte + result.value
            
            if result.fourxoneW == spielr.fourxoneW:
                punkte = punkte + result.value
            
            if result.fourxfourM == spielr.fourxfourM:
                punkte = punkte + result.value
            
            if result.fourxfourW == spielr.fourxfourW:
                punkte = punkte + result.value

            if result.fourxfourX == spielr.fourxfourX:
                punkte = punkte + result.value
            
                
        string = string + str(punkte) + "\n\r"

    context = {
        'spieler': spieler,
        'punkte': punkte,
        'string' : string
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)

def Uebersicht(request):
    spieler = Spieler.objects.all()
    results = Results.objects.all()
    erster = Results.objects.filter(rank="1")
    zweiter = Results.objects.filter(rank="2")
    dritter = Results.objects.filter(rank="3")

    context = {
        'spieler': spieler,
        'results': results,
        'erster': erster,
        'zweiter': zweiter,
        'dritter': dritter,
    }

    return render(request, 'uebersicht.html', context=context)

def Help(request):
    return render(request, 'help.html')

    

def GamesView(request):
    spiele = Games.objects.all()
    player = Players.objects.all()
    xtra = extraPoints.objects.all()
    count = []
    countx = []
    for p in player:
        temp = Games.objects.filter(winner=p.nickname).count()
        count.append(temp)

        for x in xtra:
            if x.first == p.nickname:
                temp = temp+1
            elif x.second == p.nickname:
                temp = temp+0.5
        countx.append(temp)
        

    context = {
        'spiele': spiele,
        'count': count,
        'player': player,
        'countx': countx,
        'xtra': xtra
    }
    return render(request, 'gamesView.html', context=context)
