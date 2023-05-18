from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from objects.models import Reservation
from users.models import CustomUser


# Create your models here.

class Chat(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='chat')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"

@login_required
def send_message(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        message_text = request.POST.get('message')
        if reservation_id and message_text:
            reservation = get_object_or_404(Reservation, id=reservation_id, customer=request.user)
            message = Chat(reservation=reservation, user=request.user, message=message_text)
            message.save()
            messages.success(request, 'Ваше сообщение было отправлено.')
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def get_messages(request):
    if request.method == 'GET':
        reservation_id = request.GET.get('reservation_id')
        if reservation_id:
            reservation = get_object_or_404(Reservation, id=reservation_id, customer=request.user)
            messages = reservation.chat.all()
            messages_html = render(request, 'messages.html', {'messages': messages}).content.decode('utf-8')
            return JsonResponse({'success': True, 'messages_html': messages_html})
    return JsonResponse({'success': False})