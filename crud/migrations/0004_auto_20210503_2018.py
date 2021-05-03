# Generated by Django 3.2 on 2021-05-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210428_1907'),
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
        migrations.AlterField(
            model_name='rates',
            name='title1',
            field=models.CharField(default='Бензин Аи-80 (безналичный расчет)', max_length=50, verbose_name='Бензин Аи-80 (безналичный расчет)'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='title3',
            field=models.CharField(default='Дизельное топливо (наличный расчет)', max_length=50, verbose_name='ДТ (наличный расчет)'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='title4',
            field=models.CharField(default='Мазут (Джалал-Абад) (наличный расчет)', max_length=50, verbose_name='Мазут (наличный расчет)'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='title5',
            field=models.CharField(default='Мазут (Джалал-Абад) (безналичный расчет)', max_length=50, verbose_name='Мазут (безналичный расчет)'),
        ),
    ]
