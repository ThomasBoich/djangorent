# Generated by Django 4.2.1 on 2023-06-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_alter_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
