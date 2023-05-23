from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

from users.models import CustomUser


# Create your models here.
class Object(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    #photo = models.FileField(upload_to='objects/photo/', verbose_name='Фото', blank=True, null=True)
    photo = models.ImageField(upload_to='objects/photo/', verbose_name='Photo', blank=True, null=True)
    features = models.ManyToManyField('Features', blank=True, related_name='hotels', related_query_name='hotel', verbose_name='Options')
    text = models.TextField(default='', verbose_name='Text')  # null = True, blank = True,
    slug = AutoSlugField(populate_from='name', blank=True, null=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, default='')
    city = models.ForeignKey('City', default='', on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey('Country', default='', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = 'Objects'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('object_detail', args=[self.slug])


class Features(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    icon = models.ImageField(blank=True, null=True, verbose_name="Icon", upload_to="hotels/features/icons/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['title']


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country name')
    city = models.ManyToManyField('City', verbose_name='Countries', blank=True, null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='City name')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


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
        return f"{self.guest_last_name} - {self.object.name} ({self.check_in} to {self.check_out})"

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def get_absolute_url(self):
        return reverse('reservation', args={self.id})
