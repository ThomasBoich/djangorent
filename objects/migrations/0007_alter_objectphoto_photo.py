# Generated by Django 4.2.1 on 2023-05-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_object_top_photo_alter_object_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='objects/object_photos/%Y/%m/%d/'),
        ),
    ]
