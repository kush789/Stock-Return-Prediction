# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_msft_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msft',
            old_name='bseid',
            new_name='msftid',
        ),
    ]
