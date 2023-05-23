from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from chats.models import Chat
from objects.forms import addObjectForm, ReservationEditForm
from objects.models import Object, Reservation
from users.forms import UserUpdateForm
from users.models import CustomUser


def all_objects(request):
    if request.user.is_authenticated == True:
        objects = Object.objects.all()
        context = {
            'title_page': 'Objects',
            'objects': objects,
            'count_title': Object.objects.all().count(),
            'active': 'active',
            'back_button': False,
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
            context = {'form': form, 'active': 'active','title_page': 'Adding an object',}
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
        'title_page': f'Reservations {reservations.count()}',
        'reservations': reservations,
        'reservation_consultation_count': reservations.filter(type='RC').count(),
        'reservation_consultation': reservations.filter(type='RC'),
        'reservation_order_count': reservations.filter(type='RO').count(),
        'reservation_order': reservations.filter(type='RO'),

    }
    return render(request, 'objects/reservation_list.html', context)


# def edit_reservation(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id)
#
#     if request.method == 'POST':
#         edit_form = ReservationEditForm(request.POST, instance=reservation)
#         if edit_form.is_valid():
#             edit_form.save()
#             return redirect('reservation_detail', reservation_id=reservation.id)
#     else:
#         edit_form = ReservationEditForm(instance=reservation)
#
#     context = {
#         'edit_form': edit_form,
#         'reservation': reservation,
#     }
#
#     return render(request, 'edit_reservation.html', context)


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

    if request.method == 'POST':
        manager_id = request.POST.get('manager')
        manager = CustomUser.objects.get(pk=manager_id)
        reservation.manager = manager
        reservation.save()

    if request.method == 'POST':
        edit_form = ReservationEditForm(request.POST, instance=reservation)
        if edit_form.is_valid():
            edit_form = edit_form.save(commit=False)
            return redirect('reservation', reservation_id=reservation.id)
    else:
        edit_form = ReservationEditForm(instance=reservation)

    context = {
        'title_page': f'Reservation №{reservation_id} | {reservation.guest_first_name} {reservation.guest_last_name} {reservation.guest_patronymic}',
        'reservation': reservation,
        'order': Reservation.objects.filter(id=reservation_id),
        'messages': messages,
        'managers': CustomUser.objects.all(),
        'back_button': True,
        'edit_form': edit_form,
        #'chat': Chat.objects.get(id=reservation_id)
    }
    return render(request, 'objects/reservation.html', context)

@csrf_exempt
def select_manager(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)

    if request.method == 'POST':
        value = request.POST.get('select_manager')
        print(value)
        # сохраняем значение в базу данных или как-то иначе обрабатываем
        if value is None:
            # удаление менеджера из бронирования
            print(value)
            reservation.manager == None
            reservation.save()

        else:
            # сохранение выбранного менеджера в бронирование
            manager = CustomUser.objects.get(id=value)
            reservation.manager = manager
            reservation.save()

        return JsonResponse({'Менеджер успешно изменен': True})
    else:
        return JsonResponse({'success': False, 'message': 'Метод должен быть POST'})