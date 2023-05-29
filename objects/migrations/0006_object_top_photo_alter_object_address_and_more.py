# Generated by Django 4.2.1 on 2023-05-29 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_remove_object_photo_objectphoto_object_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='top_photo',
            field=models.ImageField(blank=True, null=True, upload_to='objects/photo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='bad_ccordinates',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='coordinates',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='price_en',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='price_ru',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='text_en',
            field=models.TextField(blank=True, default='', null=True, verbose_name='En Text'),
        ),
        migrations.AlterField(
            model_name='object',
            name='text_ru',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Ru Text'),
        ),
        migrations.AlterField(
            model_name='objectphoto',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pp', to='objects.object'),
        ),
        migrations.AlterField(
            model_name='objectphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='object_photos/'),
        ),
    ]
