from django.contrib import admin

from index.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email','message')