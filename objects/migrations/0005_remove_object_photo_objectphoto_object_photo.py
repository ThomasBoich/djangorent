# Generated by Django 4.2.1 on 2023-05-26 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_rename_bad_coordinates_object_bad_ccordinates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='photo',
        ),
        migrations.CreateModel(
            name='ObjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='object_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.object')),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='photo',
            field=models.ManyToManyField(blank=True, related_name='Photos', to='objects.objectphoto', verbose_name='Photos'),
        ),
    ]
