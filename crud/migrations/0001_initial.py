# Generated by Django 3.2 on 2021-05-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('midname', models.CharField(max_length=20, verbose_name='Отчество')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('body', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Начальство',
                'verbose_name_plural': 'Начальство',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название Компании')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка на их сайт')),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Планы',
                'verbose_name_plural': 'Планы',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Достижения',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('form', models.CharField(default='Форма оплаты', max_length=255, verbose_name='Форма оплаты')),
                ('form1', models.CharField(default='Наличная', max_length=255, verbose_name='Наличная')),
                ('form2', models.CharField(default='Безналичная', max_length=255, verbose_name='Безналичная')),
                ('tax', models.CharField(default='Налоги', max_length=255, verbose_name='Налоги')),
                ('tax1', models.CharField(default='с НДС и НСП', max_length=255, verbose_name='с НДС и НСП')),
                ('tax2', models.CharField(default='с НДС, но без НСП', max_length=255, verbose_name='с НДС, но без НСП')),
                ('ai_80', models.CharField(default='Бензин Аи-80', max_length=255, verbose_name='Бензин Аи-80')),
                ('ai_price1', models.IntegerField(verbose_name='Цена аи-80 нал')),
                ('ai_price2', models.IntegerField(verbose_name='Цена аи-80 безнал')),
                ('diesel1', models.CharField(default='Дизельное топливо марки Л-0,2-40', max_length=255, verbose_name='Дизельное топливо марки Л-0,2-40')),
                ('diesel1_price1', models.IntegerField(verbose_name='Цена ДТ нал')),
                ('diesel1_price2', models.IntegerField(verbose_name='Цена ДТ безнал')),
                ('diesel2', models.CharField(default='Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С', max_length=255, verbose_name='Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С')),
                ('diesel2_price1', models.IntegerField(verbose_name='Цена ДТ с темп. застывания нал')),
                ('diesel2_price2', models.IntegerField(verbose_name='Цена ДТ с темп. застывания безнал')),
                ('fuel_oil', models.CharField(default='Мазут М-100', max_length=255, verbose_name='Мазут М-100')),
                ('fuel_price1', models.IntegerField(verbose_name='Цена Мазута нал')),
                ('fuel_price2', models.IntegerField(verbose_name='Цена Мазута безнал')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('body', models.CharField(max_length=35, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Слайды',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название таблицы')),
                ('num', models.CharField(max_length=255, null=True, verbose_name='№')),
                ('params', models.CharField(max_length=255, verbose_name='Наименование параметров')),
                ('norms', models.CharField(max_length=255, verbose_name='Нормы для нефти')),
                ('method', models.CharField(max_length=255, verbose_name='Метод испытания')),
                ('note', models.CharField(max_length=255, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Требования норм',
                'verbose_name_plural': 'Требования норм',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
