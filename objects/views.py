from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from chats.models import Chat
from objects.forms import addObjectForm, ReservationEditForm, ObjectPhotoForm
from objects.models import Object, Reservation, ObjectPhoto
from tasks.forms import TaskCommentForm
from users.forms import UserUpdateForm
from users.models import CustomUser
from tasks.models import Task
from pathlib import Path


def all_objects(request):
    ''''
        Страница всех объектов
    '''
    if request.user.is_authenticated == True:
        objects = Object.objects.all()
        context = {
            'title_page': f'Объекты {objects.count()}',
            'objects': objects,
            'count_title': Object.objects.all().count(),
            'active': 'active',
            'back_button': True,
        }
        return render(request, 'objects/index.html', context=context)
    else:
        return redirect('/')


def add_object(request):
    ''''
        Страница добавления объектов
    '''
    if request.method == 'GET':
        form = addObjectForm()
        return render(request, 'objects/add_object.html', {'form': form})

    if request.method == 'POST':
        if request.user.is_authenticated == True:
            form = addObjectForm(request.POST, request.FILES)
            photos = request.FILES.getlist('files[]')
            if form.is_valid():
                new_object = form.save(commit=False)
                new_object.save()
                for photo in photos:
                    p = ObjectPhoto.objects.create(
                        photo=photo
                    )
                    new_object.photos.add(p)

                return redirect('objects')
            else:
                form = addObjectForm()
                context = {'form': form, 'active': 'active', 'title_page': 'Adding an object'}
                return render(request, 'objects/add_object.html', context)


        else:
            return redirect('/')
    #
    #
    #     if request.method == 'POST':
    #         form = ''
    #         form = addObjectForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             obj = form.save(commit=False)
    #             obj.save()
    #             return redirect('objects')
    #     else:
    #         form = addObjectForm()
    #         context = {'form': form, 'active': 'active','title_page': 'Adding an object',}
    #         return render(request, 'objects/add_object.html', context)
    # else:
    #     return redirect('/')


# def object_detail(request, slug):
#     template = 'objects/object.html'
#     context = {
#         'object': Object.objects.get(slug=slug),
#     }
#     return render(request, template, context)


#RESERVATIONS
@login_required
def reservation_list(request):
    ''''
        Список всех бронирований
    '''
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
    '''
        Страница бронирования
    '''

    reservation = get_object_or_404(Reservation, id=reservation_id)
    messages = reservation.chatss.all()

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
        'count_tasks': Task.objects.filter(status=False).count(),
    }
    return render(request, 'objects/reservation.html', context)


@csrf_exempt
def select_manager(request, reservation_id):

    '''
        Функция добавления менеджера без перезагрузки
    '''

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

@login_required
def task_reservation(request, task_id):
    '''
       Задача внутри бронирования
    '''
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()
            return redirect('task', task_id=task_id)
    else:
        form = TaskCommentForm()

    context = {'task': task,'back_button': True, 'form': form, 'title_page': f'{task.title}'}
    return render(request, 'tasks/task_reservation.html', context)


@login_required
def tasks_reservation(request, reservation_id):
    '''
        Задачи внутри бронирования
    '''
    # reservation = Reservation.objects.get(id=reservation_id)
    reservation = get_object_or_404(Reservation, id=reservation_id)
    managers = CustomUser.objects.all()
    tasks = Task.objects.filter(status=False)
    

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

        'back_button': True,
        'title_page': f'Reservation №{reservation_id} | {reservation.guest_first_name} {reservation.guest_last_name} {reservation.guest_patronymic}',
        'reservation': reservation,
        'order': Reservation.objects.filter(id=reservation_id),
        'managers': CustomUser.objects.all(),
        'back_button': True,
        'tasks': tasks,
        'count_tasks': tasks.count(),
    }
    return render(request, 'objects/tasks_reservation.html', context)

class EditNote(UpdateView):
    model = Object
    form_class = addObjectForm
    template_name = 'objects/object.html'
    pk_url_kwarg = 'object_id'

    def get_success_url(self):
        return reverse_lazy('objects')