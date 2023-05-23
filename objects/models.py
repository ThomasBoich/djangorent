from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

from users.models import CustomUser


# Create your models here.
class Object(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    #photo = models.FileField(upload_to='objects/photo/', verbose_name='Фото', blank=True, null=True)
    photo = models.ImageField(upload_to='objects/photo/', verbose_name='Фото', blank=True, null=True)
    features = models.ManyToManyField('Features', blank=True, related_name='hotels', related_query_name='hotel', verbose_name='Опции')
    text = models.TextField(default='', verbose_name='Текст')  # null = True, blank = True,
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
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('object_detail', args=[self.slug])


class Features(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название")
    icon = models.ImageField(blank=True, null=True, verbose_name="Иконка", upload_to="hotels/features/icons/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оппция'
        verbose_name_plural = 'Опции'
        ordering = ['title']


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название страны')
    city = models.ManyToManyField('City', verbose_name='Города', blank=True, null=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Reservation(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Объект бронирования', related_name='reservations', blank=True)
    manager = models.ForeignKey(CustomUser, blank=True, null=True, related_name='order_manager', verbose_name='Ответственный', on_delete=models.CASCADE, default='')
    check_in = models.DateField(default='', verbose_name='Дата заселения', blank=True)
    check_out = models.DateField(default='', verbose_name='Дата выезда', blank=True)
    guest_last_name = models.CharField(default='', max_length=255, verbose_name='Фамилия', blank=True)
    guest_first_name = models.CharField(default='', max_length=255, verbose_name='Имя', blank=True)
    guest_patronymic = models.CharField(default='', max_length=255, verbose_name='Отчество', blank=True)
    guest_email = models.EmailField(default='', verbose_name='Емейл', blank=True)
    guest_phone = models.CharField(default='', max_length=20, verbose_name='Телефон', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='Reservation/Documents/%Y/%m/%d/', verbose_name='Договор', blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True)

    RESERVATION_ORDER = 'RO'
    RESERVATION_CONSULTATION = 'RC'

    RESERVATION_TYPE = [
        (RESERVATION_ORDER, 'Бронирование'),
        (RESERVATION_CONSULTATION, 'Консультирование')
    ]

    type = models.CharField(choices=RESERVATION_TYPE, default='', max_length=255, blank=True)

    PAID = 'PD'
    PAID_IN_PART = 'PP'
    NOT_PAID = 'NP'

    TYPE_STATUS_PAY = [
        (PAID, 'Оплачен'),
        (PAID_IN_PART, 'Оплачен частично'),
        (NOT_PAID, 'Не оплачен')
    ]

    SENT = 'ST'
    NOT_SENT = 'NS'

    TYPE_STATUS_DOCUMENTS = [
        (SENT, 'Отправлены'),
        (NOT_SENT, 'Не отправлены')
    ]

    status_pay = models.CharField(max_length=255, choices=TYPE_STATUS_PAY, default=NOT_PAID, verbose_name='Статус оплаты', blank=True)
    status_documents = models.CharField(max_length=255, choices=TYPE_STATUS_DOCUMENTS, default=NOT_SENT, verbose_name='Статус документов', blank=True)
    status_order = models.BooleanField(default=False, verbose_name='Обработана', blank=True)
    status_closed = models.BooleanField(default=False, verbose_name='Закрыта', blank=True)

    def __str__(self):
        return f"{self.guest_last_name} - {self.object.name} ({self.check_in} to {self.check_out})"

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def get_absolute_url(self):
        return reverse('reservation', args={self.id})
