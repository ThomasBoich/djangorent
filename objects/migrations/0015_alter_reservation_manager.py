# Generated by Django 4.2.1 on 2023-05-18 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('objects', '0014_reservation_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='manager',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_manager', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный'),
        ),
    ]