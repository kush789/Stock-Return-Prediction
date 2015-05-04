# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20150504_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='msft',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 10, 2, 56, 383513, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
