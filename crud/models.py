from django.db import models

# from .parser import usd_text, eur_text, rub_text, kzt_text


class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    image = models.ImageField(blank=True, null=True,verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'



class Rates(models.Model):
    date = models.DateField(auto_now=True)
    title1 = models.CharField(
        max_length=50, verbose_name='Бензин Аи-80 (безналичный расчет)',
        default='Бензин Аи-80 (безналичный расчет)')
    price1 = models.IntegerField(verbose_name='Цена')
    title2 = models.CharField(
        max_length=50, verbose_name='ДТ (безналичный расчет)',
        default='Дизельное топливо (безналичный расчет)')
    price2 = models.IntegerField(verbose_name='Цена')
    title3 = models.CharField(
        max_length=50, verbose_name='ДТ (наличный расчет)',
        default='Дизельное топливо (наличный расчет)')
    price3 = models.IntegerField(verbose_name='Цена')
    title4 = models.CharField(
        max_length=50, verbose_name='Мазут (наличный расчет)',
        default = 'Мазут (Джалал-Абад) (наличный расчет)')
    price4 = models.IntegerField(verbose_name='Цена')
    title5 = models.CharField(
        max_length=50, verbose_name='Мазут (безналичный расчет)',
        default='Мазут (Джалал-Абад) (безналичный расчет)')
    price5 = models.IntegerField(verbose_name='Цена')


    def __str__(self):
        return str(self.date)


    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'



class Leaders(models.Model):
    firstname = models.CharField(max_length=20, verbose_name='Имя')
    lastname = models.CharField(max_length=20, verbose_name='Фамилия')
    midname = models.CharField(max_length=20, verbose_name='Отчество')
    position = models.CharField(max_length=50, verbose_name="Должность")
    body = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name="Фотография")


    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.midname}"

    class Meta:
        verbose_name = 'Начальство'
        verbose_name_plural = "Начальство"


class Tables(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название Таблицы')

    def __str__(self):
        return str(self.pk)


    class Meta:
        verbose_name='Таблицы'
        verbose_name_plural="Таблицы"




class Slides(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    body = models.CharField(max_length=35, verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Слайды'
        verbose_name_plural="Слайды"

