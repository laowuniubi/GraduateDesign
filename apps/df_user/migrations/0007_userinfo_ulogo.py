# Generated by Django 2.0.7 on 2020-03-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0006_auto_20190427_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ulogo',
            field=models.FileField(default='default.jpg', upload_to='images'),
        ),
    ]