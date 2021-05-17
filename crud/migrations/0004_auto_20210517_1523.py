# Generated by Django 3.2 on 2021-05-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_tables_num'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='rates',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='price3',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='price4',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='price5',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='title3',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='title4',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='title5',
        ),
        migrations.AddField(
            model_name='rates',
            name='ai_80',
            field=models.CharField(default='Бензин Аи-80', max_length=255, verbose_name='Бензин Аи-80'),
        ),
        migrations.AddField(
            model_name='rates',
            name='diesel1',
            field=models.CharField(default='Дизельное топливо марки Л-0,2-40', max_length=255, verbose_name='Дизельное топливо марки Л-0,2-40'),
        ),
        migrations.AddField(
            model_name='rates',
            name='diesel2',
            field=models.CharField(default='Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С', max_length=255, verbose_name='Дизельное топливо марки Л-0,2. Л-0,5-40 с температурой застывания минус 30°С'),
        ),
        migrations.AddField(
            model_name='rates',
            name='form',
            field=models.CharField(default='Форма оплаты', max_length=255, verbose_name='Форма оплаты'),
        ),
        migrations.AddField(
            model_name='rates',
            name='fuel_oil',
            field=models.CharField(default='Мазут М-100', max_length=255, verbose_name='Мазут М-100'),
        ),
        migrations.AddField(
            model_name='rates',
            name='tax',
            field=models.CharField(default='Налоги', max_length=255, verbose_name='Налоги'),
        ),
    ]