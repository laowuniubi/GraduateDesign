# Generated by Django 2.0.7 on 2020-04-07 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0004_orderdetailinfo_shopername'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetailinfo',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='交易时间'),
        ),
    ]
