# Generated by Django 4.2.1 on 2023-05-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_alter_objectphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='photo',
        ),
    ]
