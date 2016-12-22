# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('neighbourhood', models.CharField(choices=[(b'LN', b'Lavington'), (b'KN', b'Karen'), (b'ND', b'Ngong Road'), (b'WY', b'Woodley')], max_length=1)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]