# Generated by Django 2.2.24 on 2021-12-04 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказ'},
        ),
    ]