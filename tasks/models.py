from django.db import models

from objects.models import Object
from users.models import CustomUser


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    text = models.TextField(verbose_name="Текст задачи")
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(verbose_name="Дата начала")
    date_finish = models.DateTimeField(verbose_name="Срок сдачи")
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Постановщик", default=1)
    executor = models.ForeignKey(CustomUser, related_name="executer_task", verbose_name="Исполнитель задачи", on_delete=models.CASCADE, blank=True, null=True,)
    object = models.ForeignKey(Object, related_name='task_object', verbose_name='Объект', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"