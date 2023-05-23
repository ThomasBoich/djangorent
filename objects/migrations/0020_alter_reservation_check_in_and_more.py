# Generated by Django 4.2.1 on 2023-05-23 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0019_reservation_status_closed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(blank=True, default='', verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(blank=True, default='', verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='deleted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Емейл'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_first_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_last_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_patronymic',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='object',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='objects.object', verbose_name='Объект бронирования'),
        ),
    ]
