# Generated by Django 4.2.1 on 2023-05-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0012_reservation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Reservation/Documents/%Y/%m/%d/', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(default='', verbose_name='Дата заселения'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(default='', verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_email',
            field=models.EmailField(default='', max_length=254, verbose_name='Емейл'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_first_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_last_name',
            field=models.CharField(default='', max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_patronymic',
            field=models.CharField(default='', max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_phone',
            field=models.CharField(default='', max_length=20, verbose_name='Телефон'),
        ),
    ]
