from django.shortcuts import render

from objects.models import Object, City


# Create your views here.

def index(request):
    template = 'index/index.html'
    all_objects = Object.objects.all().order_by('-id')[:6]
    context = {
        'top_season': all_objects,
        'cities': City.objects.all(),
    }
    return render(request, template, context)

def catalog(request):
    template = 'index/catalog.html'
    all_objects = Object.objects.all()
    context = {
        'top_season': all_objects,
        'cities': City.objects.all(),
    }
    return render(request, template, context)


def hotel(request, object_id):
    template = 'index/hotel.html'
    all_objects = Object.objects.all()
    obj = Object.objects.get(id=object_id)
    context = {
        'top_season': all_objects[:3],
        'object': obj,
        'objects': all_objects,
    }
    return render(request, template, context)