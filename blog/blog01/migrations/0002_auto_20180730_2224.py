# Generated by Django 2.0.7 on 2018-07-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='avater',
            new_name='avatar',
        ),
    ]
