# Generated by Django 4.2.1 on 2023-06-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_alter_object_name_en_alter_object_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]