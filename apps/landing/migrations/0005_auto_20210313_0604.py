# Generated by Django 3.1.7 on 2021-03-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20210306_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusimage',
            name='image',
            field=models.ImageField(upload_to='about_us_image', verbose_name='Фото'),
        ),
    ]
