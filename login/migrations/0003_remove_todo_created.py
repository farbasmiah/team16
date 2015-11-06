# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20151104_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
    ]
