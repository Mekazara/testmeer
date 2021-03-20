from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=35, verbose_name='Категория')

    class Meta:
        verbose_name = '02 - Категория продукта'
        verbose_name_plural = '02 - Категории продукта'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    image = models.ImageField(blank=True, upload_to='product_images', verbose_name='Фото')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,
                                         null=True, verbose_name='Категория')

    class Meta:
        verbose_name = '01 - Товар'
        verbose_name_plural = '01 - Товары'

    def __str__(self):
        return self.name

