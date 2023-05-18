from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from chats.models import Chat
from objects.forms import addObjectForm
from objects.models import Object, Reservation
from users.forms import UserUpdateForm
from users.models import CustomUser


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


#RESERVATIONS
@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(deleted=False)
    context = {
        'title_page': f'Бронирования {reservations.count()}',
        'reservations': reservations,
        'reservation_consultation_count': reservations.filter(type='RC').count(),
        'reservation_consultation': reservations.filter(type='RC'),
        'reservation_order_count': reservations.filter(type='RO').count(),
        'reservation_order': reservations.filter(type='RO'),

    }
    return render(request, 'objects/reservation_list.html', context)
@csrf_exempt
def reservation(request, reservation_id):
    # reservation = Reservation.objects.get(id=reservation_id)
    reservation = get_object_or_404(Reservation, id=reservation_id)
    messages = reservation.chat.all()
    managers = CustomUser.objects.all()
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            message = Chat(reservation=reservation, user=request.user, message=message_text)
            message.save()
            # messages.success(request, 'Ваше сообщение было отправлено.')
            return redirect('reservation', reservation_id=reservation.id)
        else:
            # messages.error(request, 'Пожалуйста, введите текст сообщения.')
            pass

    # if request.method == 'POST':
    #     user_form = UserUpdateForm(request.POST, instance=request.user)
    #     password_form = PasswordChangeForm(request.user, request.POST)
    #     if user_form.is_valid() and password_form.is_valid():
    #         user_form.save()
    #         password_form.save()
    #         messages.success(request, 'Профиль успешно обновлен')
    #         return redirect('profile')
    # else:
    #     user_form = UserUpdateForm(instance=request.user)
    #     password_form = PasswordChangeForm(request.user)
    # return render(request, 'update_profile.html', {'user_form': user_form, 'password_form': password_form})
    if request.method == 'POST':
        manager_id = request.POST.get('manager')
        manager = CustomUser.objects.get(pk=manager_id)
        reservation.manager = manager
        reservation.save()

    context = {
        'title_page': f'Заявка №{reservation_id}',
        'reservation': reservation,
        'order': Reservation.objects.filter(id=reservation_id),
        'messages': messages,
        'managers': CustomUser.objects.all(),
        #'chat': Chat.objects.get(id=reservation_id)
    }
    return render(request, 'objects/reservation.html', context)

@csrf_exempt
def save_select(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    managers = CustomUser.objects.all()

    if request.method == 'POST':
        value = request.POST.get('select_value')
        # сохраняем значение в базу данных или как-то иначе обрабатываем
        manager = CustomUser.objects.get(id=value)
        if value is None:
            # удаление менеджера из бронирования
            reservation.manager = None
            reservation.save()
        else:
            # сохранение выбранного менеджера в бронирование
            manager = CustomUser.objects.get(id=value)
            reservation.manager = manager
            reservation.save()
