from django.shortcuts import render, redirect

from index.forms import ContactForm
from index.models import Contact
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

def about(request):
    template = 'index/about.html'
    context = {
        'title': 'About',
    }
    return render(request, template, context)

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Создание объекта модели Contact и сохранение его в базе данных
            contact = Contact(name=name, phone=phone, email=email, message=message)
            contact.save()
            # Перенаправлениедля предотвращения повторной отправки формы
            return redirect('contacts')
    else:
        form = ContactForm()

    template = 'index/contacts.html'
    context = {
        'title': 'Contcts','form': form,
    }
    return render(request, template, context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Создание объекта модели Contact и сохранение его в базе данных
            contact = Contact(name=name, phone=phone, email=email, message=message)
            contact.save()
            # Перенаправлениедля предотвращения повторной отправки формы
            return redirect('success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)
