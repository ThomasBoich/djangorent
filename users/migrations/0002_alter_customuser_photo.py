# Generated by Django 4.2.1 on 2023-05-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, default='../static/assets/default_avatar.png', upload_to='midia/users/%Y/%m/%d/', verbose_name='Аватар'),
        ),
    ]
