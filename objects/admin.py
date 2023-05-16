from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import addObjectForm
# Register your models here.
from .models import Object, Features, Reservation


class ObjectAdmin(admin.ModelAdmin):
    form = addObjectForm
    list_display = ('name', 'photo_img', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.sender = request.user
    #     super().save_model(request, obj, form, change)

    def photo_img(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.photo.url,
            width=70,
            height=70,
        ))
    photo_img.short_description = 'Photo'

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest_last_name', 'guest_first_name', 'object', 'check_in', 'check_out')
    list_filter = ('object', 'check_in', 'check_out')
    search_fields = ('guest_last_name', 'guest_first_name', 'guest_email', 'guest_phone')

admin.site.register(Reservation, ReservationAdmin)

admin.site.register(Object, ObjectAdmin)
admin.site.register(Features, FeaturesAdmin)