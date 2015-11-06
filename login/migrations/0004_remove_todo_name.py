# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_todo_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
    ]
