from admin_actions.admin import ActionsModelAdmin
#from multiupload.admin import MultiUploadAdminMixin MultiUploadAdminMixin,
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .forms import addObjectForm
# Register your models here.
from .models import Object, Features, Reservation, Country, City, ObjectPhoto, FeaturesCategory


# class ImageInline(admin.StackedInline):
#     model = ObjectPhoto


class ObjectAdmin(admin.ModelAdmin):
    form = addObjectForm
    fields = (
        'name_ru', 'name_en', 'top_photo',
        'features_ru',
        'features_en','text_ru',
        'text_en','description_ru',
        'description_en','address','coordinates_x', 'coordinates_y','bad_coordinates_x','bad_coordinates_y',
        'city_ru','city_en','country_ru','country_en',
        'price_ru','price_en','rating', 'photos')
    list_display = ('name_en', 'slug')
    filter_horizontal = ('photos',)
    search_fields = ('name_en',)
    prepopulated_fields = {'slug': ('name_en',)}
    # inlines = [ImageInline]
    readonly_fields = ['image_tag']
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" />'.format(obj.top_photo.url))
    # multiupload_form = ObjectPhotoForm
    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.sender = request.user
    #     super().save_model(request, obj, form, change)

    def photo_img(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.top_photo.url,
            width=70,
            height=70,
        ))
    photo_img.short_description = 'Photo'

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('title_en',)
    search_fields = ('title_en',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_en',)
    search_fields = ('name_en',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name_en',)
    search_fields = ('name_en',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest_last_name', 'guest_first_name', 'object', 'check_in', 'check_out')
    list_filter = ('object', 'check_in', 'check_out')
    search_fields = ('guest_last_name', 'guest_first_name', 'guest_email', 'guest_phone')

class FeaturesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')

admin.site.register(ObjectPhoto)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(FeaturesCategory, FeaturesCategoryAdmin)