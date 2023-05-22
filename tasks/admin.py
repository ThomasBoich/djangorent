from django.contrib import admin
from .models import Task, TaskComment


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('author',)
    search_fields = ('author',)