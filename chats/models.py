from django.db import models

from objects.models import Reservation
from users.models import CustomUser


# Create your models here.

class Chat(models.Model):
    order = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='chat')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"