from django.shortcuts import render

from objects.models import Object


# Create your views here.

def index(request):
    template = 'index/index.html'
    all_objects = Object.objects.all()
    context = {
        'top_season': all_objects,
    }
    return render(request, template, context)