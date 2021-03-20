# Generated by Django 3.1.7 on 2021-03-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '01 - Товар', 'verbose_name_plural': '01 - Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': '02 - Категория продукта', 'verbose_name_plural': '02 - Категории продукта'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images', verbose_name='Фото'),
        ),
    ]