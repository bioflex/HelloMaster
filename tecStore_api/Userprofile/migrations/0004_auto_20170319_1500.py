# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0003_auto_20170213_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='first_img',
            field=models.ImageField(default='Images/None/no-img.png', null=True, upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='second_img',
            field=models.ImageField(default='Images/None/no-img.png', null=True, upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='third_img',
            field=models.ImageField(default='Images/None/no-img.png', null=True, upload_to='Images/'),
        ),
    ]
