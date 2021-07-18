# Generated by Django 3.2 on 2021-06-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20210528_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaders',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='firstname_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='firstname_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='lastname_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='lastname_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='midname_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='midname_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='position_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='leaders',
            name='position_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='news',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='news',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='plans',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='plans',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='plans',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='plans',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='progress',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='progress',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='progress',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='progress',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='slides',
            name='body_en',
            field=models.CharField(max_length=35, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='slides',
            name='body_ru',
            field=models.CharField(max_length=35, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='slides',
            name='title_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='slides',
            name='title_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='social',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='social',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='social',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='social',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tables',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название таблицы'),
        ),
        migrations.AddField(
            model_name='tables',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название таблицы'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]