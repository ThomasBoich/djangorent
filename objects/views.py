from django.shortcuts import render, redirect
from objects.forms import addObjectForm
from objects.models import Object


def all_objects(request):
    if request.user.is_authenticated == True:
        objects = Object.objects.all()
        context = {
            'title_page': 'Объекты',
            'objects': objects,
            'count_title': Object.objects.all().count(),
            'active': 'active',
        }
        return render(request, 'objects/index.html', context=context)
    else:
        return redirect('/')

def add_object(request):
    if request.user.is_authenticated == True:
        form = ''
        form = addObjectForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('objects')
        else:
            form = addObjectForm()
            context = {'form': form, 'active': 'active','title_page': 'Добавление объекта',}
            return render(request, 'objects/add_object.html', context)
    else:
        return redirect('/')


def object_detail(request, slug):
    template = 'objects/object.html'
    context = {
        'object': Object.objects.get(slug=slug),
    }
    return render(request, template, context)