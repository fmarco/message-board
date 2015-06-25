# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20150623_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='post',
            new_name='message',
        ),
    ]
