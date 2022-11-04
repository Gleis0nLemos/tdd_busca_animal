from django.shortcuts import render
from animals.models import Animal

def index(request):

    context = {'caracteristicas': Animal.objects.all()}
    return render(request, 'index.html', context)