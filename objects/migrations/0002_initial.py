# Generated by Django 4.2.1 on 2023-05-29 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='manager',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_manager', to=settings.AUTH_USER_MODEL, verbose_name='Manager'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='object',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='objects.object', verbose_name='Object Reservation'),
        ),
        migrations.AddField(
            model_name='objectphoto',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pp', to='objects.object'),
        ),
        migrations.AddField(
            model_name='object',
            name='city_en',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_en', to='objects.city'),
        ),
        migrations.AddField(
            model_name='object',
            name='city_ru',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_ru', to='objects.city'),
        ),
        migrations.AddField(
            model_name='object',
            name='country_en',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_en', to='objects.country'),
        ),
        migrations.AddField(
            model_name='object',
            name='country_ru',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_ru', to='objects.country'),
        ),
        migrations.AddField(
            model_name='object',
            name='features_en',
            field=models.ManyToManyField(blank=True, related_name='hotels_en', related_query_name='hotel_en', to='objects.features', verbose_name='En Options'),
        ),
        migrations.AddField(
            model_name='object',
            name='features_ru',
            field=models.ManyToManyField(blank=True, related_name='hotels_ru', related_query_name='hotel_ru', to='objects.features', verbose_name='Ru Options'),
        ),
        migrations.AddField(
            model_name='object',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='Photos', to='objects.objectphoto', verbose_name='Photos'),
        ),
        migrations.AddField(
            model_name='features',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.featurescategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='country',
            name='city_en',
            field=models.ManyToManyField(blank=True, null=True, related_name='county_city_en', to='objects.city', verbose_name='En Countries'),
        ),
        migrations.AddField(
            model_name='country',
            name='city_ru',
            field=models.ManyToManyField(blank=True, null=True, related_name='county_city_ru', to='objects.city', verbose_name='Ru Countries'),
        ),
    ]
