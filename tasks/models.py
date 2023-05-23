from django.db import models
from django.urls import reverse

from objects.models import Object
from users.models import CustomUser


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Task name")
    text = models.TextField(verbose_name="Task text")
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(verbose_name="Date start")
    date_finish = models.DateTimeField(verbose_name="Date finish")
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Owner", default=1)
    executor = models.ForeignKey(CustomUser, related_name="executer_task", verbose_name="Executor", on_delete=models.CASCADE, blank=True, null=True,)
    object = models.ForeignKey(Object, related_name='task_object', verbose_name='Object', on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='Success')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.id},)


class TaskComment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)