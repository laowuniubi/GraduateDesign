# Generated by Django 2.0.7 on 2020-04-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0009_auto_20200403_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='ucheck_pass_or_fail',
            new_name='ucheck_passOrfail',
        ),
    ]
