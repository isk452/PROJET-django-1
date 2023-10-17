from django.http import HttpResponse
from listings.models import Band  # Importez le modèle Band depuis l'application 'listings'
from django.shortcuts import render

def hello(request):
    objet = Band.objects.first()  # Exemple : récupérer le premier objet du modèle Band
    return render(request, 'hello.html', {'objet': objet})

def about(request):
    return HttpResponse('<h1>À propos</h1>  <p>Nous adorons merch !</p>')
