# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_todo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='createdby',
            field=models.CharField(default=b'admin', max_length=100),
        ),
    ]
