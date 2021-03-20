from django.db import models
# from singleton_models import singletonmodel

class Logo(models.Model):
    logo = models.ImageField(verbose_name='Логотип', upload_to='logos')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'

    def __str__(self):
        return 'Логотип'

class Content(models.Model):
    title = models.CharField(max_length=32, verbose_name='Заголовок')
    description = models.TextField(max_length=128, verbose_name='Описание')
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True,
                             blank=True, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    def __str__(self):
        return f'{self.title}'



class AboutUs(models.Model):
    title = models.CharField(max_length=32, verbose_name='Заголовок')
    sub_title = models.CharField(verbose_name='Подзаголовок', max_length=32)
    description = models.TextField(max_length=132, verbose_name='Описание')
    video = models.FileField(upload_to='videos', verbose_name='Видео')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

class AboutUsImage(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='about_us_image')
    about_us_id = models.ForeignKey(AboutUs, on_delete=models.SET_NULL, null=True,
                                    blank=True, verbose_name='О нас')

    class Meta:
        verbose_name = 'Фото о нас'
        verbose_name_plural = 'Фото о нас'

    def __str__(self):
        return 'Фото о нас'