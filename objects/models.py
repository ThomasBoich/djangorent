from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Object(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name='Ru Name', blank=True, null=True)
    name_en = models.CharField(max_length=255, verbose_name='En Name', blank=True, null=True)
    top_photo = models.ImageField(upload_to='objects/photo/%Y/%m/%d/', blank=True, null=True)
    photos = models.ManyToManyField('ObjectPhoto', blank=True, verbose_name='Photos', related_name='Photos')
    features_ru = models.ManyToManyField('Features', blank=True, related_name='hotels_ru', related_query_name='hotel_ru', verbose_name='Ru Options')
    features_en = models.ManyToManyField('Features', blank=True, related_name='hotels_en', related_query_name='hotel_en', verbose_name='En Options')
    text_ru = models.TextField(default='', verbose_name='Ru Text', null = True, blank = True,)  #
    text_en = models.TextField(default='', verbose_name='En Text', null = True, blank = True)  # ,
    slug = AutoSlugField(populate_from='name_en', blank=True, null=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    address = models.CharField(max_length=255, default='', blank=True, null=True)
    coordinates_x = models.CharField(max_length=255, default='', blank=True, null=True)
    coordinates_y = models.CharField(max_length=255, default='', blank=True, null=True)
    bad_coordinates_x = models.CharField(max_length=255, default='', blank=True, null=True)
    bad_coordinates_y = models.CharField(max_length=255, default='', blank=True, null=True)
    city_ru = models.ForeignKey('City', related_name='city_ru', default='', on_delete=models.CASCADE, blank=True, null=True)
    city_en = models.ForeignKey('City', related_name='city_en', default='', on_delete=models.CASCADE, blank=True, null=True)
    country_ru = models.ForeignKey('Country', related_name='country_ru', default='', on_delete=models.CASCADE, blank=True, null=True)
    country_en = models.ForeignKey('Country', related_name='country_en', default='', on_delete=models.CASCADE, blank=True, null=True)
    price_ru = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_en = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name_en}'

    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = 'Objects'
        ordering = ['name_en']

    def get_absolute_url(self):
        return reverse('object_detail', args=[self.slug])

    def get_photos(self):
        return ", ".join([str(p) for p in self.photo.all()])



class ObjectPhoto(models.Model):
    photo = models.ImageField(upload_to='objects/object_photos/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Features(models.Model):
    title_ru = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    title_en = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    icon = models.ImageField(blank=True, null=True, verbose_name="Icon", upload_to="hotels/features/icons/")
    category = models.ForeignKey('FeaturesCategory', blank=True, null=True, verbose_name='Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_ru}'

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['title_en']


class FeaturesCategory(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='name_ru')
    name_en = models.CharField(max_length=100, verbose_name='name_en')

    def __str__(self):
        return f'{self.name_en}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Country(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Ru Country name', blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='En Country name', blank=True, null=True)
    city_ru = models.ManyToManyField('City', related_name='county_city_ru', verbose_name='Ru Countries', blank=True, null=True)
    city_en = models.ManyToManyField('City', related_name='county_city_en', verbose_name='En Countries', blank=True, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name_en}'


class City(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Ru City name',blank=True, null=True)
    name_en = models.CharField(max_length=100, verbose_name='En City name',blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name_en}'


## БРОНИРОВАНИЯ
class Reservation(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Object Reservation', related_name='reservations', blank=True)
    manager = models.ForeignKey(CustomUser, blank=True, null=True, related_name='order_manager', verbose_name='Manager', on_delete=models.CASCADE, default='')
    check_in = models.DateField(default='', verbose_name='check_in', blank=True)
    check_out = models.DateField(default='', verbose_name='check_out', blank=True)
    guest_last_name = models.CharField(default='', max_length=255, verbose_name='guest_last_nam', blank=True)
    guest_first_name = models.CharField(default='', max_length=255, verbose_name='guest_first_name', blank=True)
    guest_patronymic = models.CharField(default='', max_length=255, verbose_name='guest_patronymic', blank=True)
    guest_email = models.EmailField(default='', verbose_name='guest_email', blank=True)
    guest_phone = models.CharField(default='', max_length=20, verbose_name='guest_phone', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='Reservation/Documents/%Y/%m/%d/', verbose_name='document', blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True)

    RESERVATION_ORDER = 'RO'
    RESERVATION_CONSULTATION = 'RC'

    RESERVATION_TYPE = [
        (RESERVATION_ORDER, 'Reservation'),
        (RESERVATION_CONSULTATION, 'Consultation')
    ]

    type = models.CharField(choices=RESERVATION_TYPE, default='', max_length=255, blank=True)

    PAID = 'PD'
    PAID_IN_PART = 'PP'
    NOT_PAID = 'NP'

    TYPE_STATUS_PAY = [
        (PAID, 'Paid'),
        (PAID_IN_PART, 'Paid in part'),
        (NOT_PAID, 'Not paid')
    ]

    SENT = 'ST'
    NOT_SENT = 'NS'

    TYPE_STATUS_DOCUMENTS = [
        (SENT, 'Sent'),
        (NOT_SENT, 'Non sent')
    ]

    status_pay = models.CharField(max_length=255, choices=TYPE_STATUS_PAY, default=NOT_PAID, verbose_name='Payment State', blank=True)
    status_documents = models.CharField(max_length=255, choices=TYPE_STATUS_DOCUMENTS, default=NOT_SENT, verbose_name='Document Status', blank=True)
    status_order = models.BooleanField(default=False, verbose_name='Success', blank=True)
    status_closed = models.BooleanField(default=False, verbose_name='Closed', blank=True)

    def __str__(self):
        return f"{self.guest_last_name} - {self.object.name_en} ({self.check_in} to {self.check_out})"

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def get_absolute_url(self):
        return reverse('reservation', args={self.id})
