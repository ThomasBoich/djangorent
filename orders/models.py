from django.db import models

from objects.models import Object
from users.models import CustomUser

# Create your models here.

class Order(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Объект бронирования')
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Заказчик')
    manager = models.ForeignKey(CustomUser, related_name='order_manager', verbose_name='Ответственный', on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)

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

    status_pay = models.CharField(max_length=255, choices=TYPE_STATUS_PAY, default=NOT_PAID, verbose_name='Статус оплаты')
    status_documents = models.CharField(max_length=255, choices=TYPE_STATUS_DOCUMENTS, default=NOT_SENT, verbose_name='Статус документов')
    status_order = models.BooleanField(default=True, verbose_name='Статус сделки')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f'{self.object.name}, {self.customer.name}'