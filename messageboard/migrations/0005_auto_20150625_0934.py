# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0004_auto_20150624_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to=b'%Y/%m/%d', blank=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
