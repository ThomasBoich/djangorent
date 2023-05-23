# Generated by Django 4.2.1 on 2023-05-23 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('objects', '0021_alter_reservation_status_closed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'ordering': ['title'], 'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['name'], 'verbose_name': 'Object', 'verbose_name_plural': 'Objects'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, verbose_name='City name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='city',
            field=models.ManyToManyField(blank=True, null=True, to='objects.city', verbose_name='Countries'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Country name'),
        ),
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='hotels/features/icons/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='features',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='object',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='hotels', related_query_name='hotel', to='objects.features', verbose_name='Options'),
        ),
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='object',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='objects/photo/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='object',
            name='text',
            field=models.TextField(default='', verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(blank=True, default='', verbose_name='check_in'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(blank=True, default='', verbose_name='check_out'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Reservation/Documents/%Y/%m/%d/', verbose_name='document'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='guest_email'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_first_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='guest_first_name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_last_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='guest_last_nam'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_patronymic',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='guest_patronymic'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='guest_phone'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='manager',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_manager', to=settings.AUTH_USER_MODEL, verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='object',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='objects.object', verbose_name='Object Reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status_closed',
            field=models.BooleanField(blank=True, default=False, verbose_name='Closed'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status_documents',
            field=models.CharField(blank=True, choices=[('ST', 'Sent'), ('NS', 'Non sent')], default='NS', max_length=255, verbose_name='Document Status'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status_order',
            field=models.BooleanField(blank=True, default=False, verbose_name='Success'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('PD', 'Paid'), ('PP', 'Paid in part'), ('NP', 'Not paid')], default='NP', max_length=255, verbose_name='Payment State'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='type',
            field=models.CharField(blank=True, choices=[('RO', 'Reservation'), ('RC', 'Consultation')], default='', max_length=255),
        ),
    ]