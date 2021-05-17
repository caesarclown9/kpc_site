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
    form = models.CharField(max_length=255, default='Форма оплаты', verbose_name='Форма оплаты')
    tax = models.CharField(max_length=255, default='Налоги', verbose_name='Налоги')
    ai_80 = models.CharField(max_length=255, default='Бензин Аи-80', verbose_name="Бензин Аи-80")
    diesel1 = models.CharField(max_length=255, default='Дизельное топливо марки Л-0,2-40', verbose_name='Дизельное топливо марки Л-0,2-40')
    diesel2 = models.CharField(max_length=255, default="Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С", verbose_name="Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С")
    fuel_oil = models.CharField(max_length=255, default='Мазут М-100', verbose_name='Мазут М-100')

    def __str__(self):
        return str(self.date)


    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class RatesDetails(models.Model):
    name = models.CharField(max_length=255)



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
    name = models.CharField(max_length=255, verbose_name='Название таблицы')
    num = models.CharField(max_length=255, verbose_name='№', null=True)
    params = models.CharField(max_length=255, verbose_name="Наименование параметров")
    norms = models.CharField(max_length=255, verbose_name='Нормы для нефти')
    method = models.CharField(max_length=255, verbose_name="Метод испытания")
    note = models.CharField(max_length=255, verbose_name="Примечание")

    def __str__(self):
        return str(self.name)


    class Meta:
        # db_table = "Norms_requirements"
        verbose_name='Требования норм'
        verbose_name_plural="Требования норм"




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


class Testimonials(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name="Должность")
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name="Фото")


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class Partners(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название Компании')
    link = models.CharField(max_length=255, verbose_name='Ссылка на их сайт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'



class Plans(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Планы'
        verbose_name_plural = 'Планы'


class Progress(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'