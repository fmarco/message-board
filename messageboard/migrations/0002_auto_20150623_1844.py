# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'%Y/%m/%d')),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date',)},
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(related_name='photos', to='messageboard.Message'),
        ),
    ]
