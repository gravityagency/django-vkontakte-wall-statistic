# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_wall_statistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreach',
            name='hide',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='join_group',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='links',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='reach_subscribers',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='reach_total',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='report',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='to_group',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postreach',
            name='unsubscribe',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
