from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    image = models.FileField(blank=True, null=True,verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/news/')

    def __str__(self):
        return self.news.title


class Social(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    image = models.FileField(blank=True, null=True,verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальная ответственность'
        verbose_name_plural = 'Социальная ответственность'


class SocialImage(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='social/news/')

    def __str__(self):
        return self.social.title

class Rates(models.Model):
    date = models.DateField(auto_now=True)
    price1 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена аи-80 нал', blank=True, null=True)
    price2 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена аи-80 безнал', blank=True, null=True)
    diesel_price1 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена ДТ нал', blank=True, null=True)
    diesel_price2 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена ДТ безнал', blank=True, null=True)
    diesel_price3 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена ДТ с темп. застывания нал', blank=True, null=True)
    diesel_price4 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена ДТ с темп. застывания безнал', blank=True, null=True)
    fuel_price1 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена Мазута нал', blank=True, null=True)
    fuel_price2 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена Мазута безнал', blank=True, null=True)

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
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.midname}"

    class Meta:
        verbose_name = 'Начальство'
        verbose_name_plural = "Начальство"


class Tables(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название таблицы')


    def __str__(self):
        return str(self.name)


    class Meta:
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
    image = models.FileField(blank=True, null=True, verbose_name="Картинка")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Планы'
        verbose_name_plural = 'Планы'


class PlansImage(models.Model):
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/plans/')

    def __str__(self):
        return self.plans.title


class Progress(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    image = models.FileField(blank=True, null=True, verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'


class ProgressImage(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/progress/')

    def __str__(self):
        return self.progress.title