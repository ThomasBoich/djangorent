from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from chats.models import Chat
from objects.models import Reservation

# Create your views here.
@login_required
def chat(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, customer=request.user)
    messages = reservation.chat.all()
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            message = Chat(reservation=reservation, user=request.user, message=message_text)
            message.save()
            messages.success(request, 'Ваше сообщение было отправлено.')
            return redirect('chat', reservation_id=reservation.id)
        else:
            messages.error(request, 'Пожалуйста, введите текст сообщения.')
    return render(request, 'chat.html', {'reservation': reservation, 'messages': messages})