# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkontakte_wall', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReach',
            fields=[
                ('fetched', models.DateTimeField(db_index=True, null=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e', blank=True)),
                ('post', models.OneToOneField(related_name='reach', primary_key=True, serialize=False, to='vkontakte_wall.Post', verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('hide', models.PositiveIntegerField()),
                ('join_group', models.PositiveIntegerField()),
                ('links', models.PositiveIntegerField()),
                ('reach_subscribers', models.PositiveIntegerField()),
                ('reach_total', models.PositiveIntegerField()),
                ('report', models.PositiveIntegerField()),
                ('to_group', models.PositiveIntegerField()),
                ('unsubscribe', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Vkontakte post reach',
                'verbose_name_plural': 'Vkontakte post reaches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostStatistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fetched', models.DateTimeField(db_index=True, null=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e', blank=True)),
                ('reach', models.PositiveIntegerField(default=0, verbose_name='\u041f\u043e\u043b\u043d\u044b\u0439 \u043e\u0445\u0432\u0430\u0442')),
                ('reach_subscribers', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a\u043e\u0432')),
                ('link_clicks', models.PositiveIntegerField(default=0, verbose_name='\u041a\u043b\u0438\u043a\u0438 \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c')),
                ('reach_males', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c')),
                ('reach_females', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c')),
                ('reach_age_18', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u0434\u043e 18')),
                ('reach_age_18_21', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 18 \u0434\u043e 21')),
                ('reach_age_21_24', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 21 \u0434\u043e 24')),
                ('reach_age_24_27', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 24 \u0434\u043e 27')),
                ('reach_age_27_30', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 27 \u0434\u043e 30')),
                ('reach_age_30_35', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 30 \u0434\u043e 35')),
                ('reach_age_35_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 35 \u0434\u043e 45')),
                ('reach_age_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0443 \u043e\u0442 45')),
                ('reach_males_age_18', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u0434\u043e 18')),
                ('reach_males_age_18_21', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 18 \u0434\u043e 21')),
                ('reach_males_age_21_24', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 21 \u0434\u043e 24')),
                ('reach_males_age_24_27', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 24 \u0434\u043e 27')),
                ('reach_males_age_27_30', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 27 \u0434\u043e 30')),
                ('reach_males_age_30_35', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 30 \u0434\u043e 35')),
                ('reach_males_age_35_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 35 \u0434\u043e 45')),
                ('reach_males_age_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u043c\u0443\u0436\u0447\u0438\u043d\u0430\u043c \u043e\u0442 45')),
                ('reach_females_age_18', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u0434\u043e 18')),
                ('reach_females_age_18_21', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 18 \u0434\u043e 21')),
                ('reach_females_age_21_24', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 21 \u0434\u043e 24')),
                ('reach_females_age_24_27', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 24 \u0434\u043e 27')),
                ('reach_females_age_27_30', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 27 \u0434\u043e 30')),
                ('reach_females_age_30_35', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 30 \u0434\u043e 35')),
                ('reach_females_age_35_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 35 \u0434\u043e 45')),
                ('reach_females_age_45', models.PositiveIntegerField(default=0, verbose_name='\u041e\u0445\u0432\u0430\u0442 \u043f\u043e \u0436\u0435\u043d\u0449\u0438\u043d\u0430\u043c \u043e\u0442 45')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430', db_index=True)),
                ('period', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u041f\u0435\u0440\u0438\u043e\u0434', choices=[(1, '\u0414\u0435\u043d\u044c'), (30, '\u041c\u0435\u0441\u044f\u0446')])),
                ('post', models.ForeignKey(related_name='statistics', verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435', to='vkontakte_wall.Post')),
            ],
            options={
                'verbose_name': 'Vkontakte post statistic',
                'verbose_name_plural': 'Vkontakte post statistics',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='poststatistic',
            unique_together=set([('post', 'date', 'period')]),
        ),
    ]
