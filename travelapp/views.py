from .models import Place, Teams

from django.shortcuts import render

# Create your views here.


def demo(request):
    obj1 = Place.objects.all()
    obj2 = Teams.objects.all()
    return render(request, 'index.html', {'result': obj1, 'team': obj2})
