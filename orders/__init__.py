from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['object', 'customer', 'status_pay', 'status_documents', 'status_order', 'creation_date']
    list_filter = ['status_pay', 'status_documents', 'status_order', 'creation_date']
    search_fields = ['object__name', 'customer__name']