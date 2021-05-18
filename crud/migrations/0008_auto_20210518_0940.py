# Generated by Django 3.2 on 2021-05-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20210518_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='diesel_price1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена ДТ нал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='diesel_price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена ДТ безнал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='diesel_price3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена ДТ с темп. застывания нал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='diesel_price4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена ДТ с темп. застывания безнал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='fuel_price1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена Мазута нал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='fuel_price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена Мазута безнал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='price1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена аи-80 нал'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Цена аи-80 безнал'),
        ),
    ]
