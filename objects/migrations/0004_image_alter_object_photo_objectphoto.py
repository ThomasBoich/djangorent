# Generated by Django 4.2.1 on 2023-05-15 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_alter_object_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='objects/photo/')),
            ],
        ),
        migrations.AlterField(
            model_name='object',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='objects/photo/', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='ObjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='objects/photo/', verbose_name='Фото')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='objects.object')),
            ],
        ),
    ]
