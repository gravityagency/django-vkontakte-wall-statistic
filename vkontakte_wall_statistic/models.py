# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import Signal
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured
from vkontakte_api.models import VkontakteManager, VkontakteModel, VkontakteDeniedAccessError, VkontakteContentError
from vkontakte_wall.models import Post
from datetime import datetime
from urllib import unquote
import simplejson as json
import logging
import re

log = logging.getLogger('vkontakte_wall_statistic')


class PostStatisticRemoteManager(VkontakteManager):

    def fetch(self, post, date_from, date_to, *args, **kwargs):
        kwargs['group_id'] = post.wall_owner.remote_id
        kwargs['post_id'] = post.remote_id_short
        kwargs['extra_fields'] = {'post_id': post.id}
        return super(PostStatisticRemoteManager, self).fetch(*args, **kwargs)


class PostStatisticAbstract(models.Model):
    class Meta:
        abstract = True

    reach = models.PositiveIntegerField(u'Полный охват', null=True)
    reach_subsribers = models.PositiveIntegerField(u'Охват подписчиков', null=True)
    link_clicks = models.PositiveIntegerField(u'Клики по ссылкам', null=True)

    reach_males = models.PositiveIntegerField(u'Охват по мужчинам', null=True)
    reach_females = models.PositiveIntegerField(u'Охват по женщинам', null=True)

    reach_age_18 = models.PositiveIntegerField(u'Охват по возрасту до 18', null=True)
    reach_age_18_21 = models.PositiveIntegerField(u'Охват по возрасту от 18 до 21', null=True)
    reach_age_21_24 = models.PositiveIntegerField(u'Охват по возрасту от 21 до 24', null=True)
    reach_age_24_27 = models.PositiveIntegerField(u'Охват по возрасту от 24 до 27', null=True)
    reach_age_27_30 = models.PositiveIntegerField(u'Охват по возрасту от 27 до 30', null=True)
    reach_age_30_35 = models.PositiveIntegerField(u'Охват по возрасту от 30 до 35', null=True)
    reach_age_35_45 = models.PositiveIntegerField(u'Охват по возрасту от 35 до 45', null=True)
    reach_age_45 = models.PositiveIntegerField(u'Охват по возрасту от 45', null=True)

    reach_males_age_18 = models.PositiveIntegerField(u'Охват по мужчинам до 18', null=True)
    reach_males_age_18_21 = models.PositiveIntegerField(u'Охват по мужчинам от 18 до 21', null=True)
    reach_males_age_21_24 = models.PositiveIntegerField(u'Охват по мужчинам от 21 до 24', null=True)
    reach_males_age_24_27 = models.PositiveIntegerField(u'Охват по мужчинам от 24 до 27', null=True)
    reach_males_age_27_30 = models.PositiveIntegerField(u'Охват по мужчинам от 27 до 30', null=True)
    reach_males_age_30_35 = models.PositiveIntegerField(u'Охват по мужчинам от 30 до 35', null=True)
    reach_males_age_35_45 = models.PositiveIntegerField(u'Охват по мужчинам от 35 до 45', null=True)
    reach_males_age_45 = models.PositiveIntegerField(u'Охват по мужчинам от 45', null=True)

    reach_females_age_18 = models.PositiveIntegerField(u'Охват по женщинам до 18', null=True)
    reach_females_age_18_21 = models.PositiveIntegerField(u'Охват по женщинам от 18 до 21', null=True)
    reach_females_age_21_24 = models.PositiveIntegerField(u'Охват по женщинам от 21 до 24', null=True)
    reach_females_age_24_27 = models.PositiveIntegerField(u'Охват по женщинам от 24 до 27', null=True)
    reach_females_age_27_30 = models.PositiveIntegerField(u'Охват по женщинам от 27 до 30', null=True)
    reach_females_age_30_35 = models.PositiveIntegerField(u'Охват по женщинам от 30 до 35', null=True)
    reach_females_age_35_45 = models.PositiveIntegerField(u'Охват по женщинам от 35 до 45', null=True)
    reach_females_age_45 = models.PositiveIntegerField(u'Охват по женщинам от 45', null=True)


class PostStatistic(PostStatisticAbstract):
    '''
    Post statistic model collecting information
    '''
    class Meta:
        verbose_name = _('Vkontakte post statistic')
        verbose_name_plural = _('Vkontakte post statistics')
        unique_together = ('post', 'date', 'period')

    methods_namespace = 'stats'

    post = models.ForeignKey(Post, verbose_name=u'Сообщение', related_name='statistics')
    date = models.DateField(u'Дата', db_index=True)
    period = models.PositiveSmallIntegerField(u'Период', choices=((1, u'День'),(30, u'Месяц'),), default=1, db_index=True)

    objects = models.Manager()
    remote = PostStatisticRemoteManager(remote_pk=('post','date'), methods={
        'get': 'getPostStats',
    })

    def parse(self, response):
        '''
        Transform response for correct parsing it in parent method
        '''
        response['date'] = response.pop('day')

        fields_map = {
            'sex': {
                'f': 'females',
                'm': 'males',
            },
            'age': {
                '12-18': 'age_18',
                '18-21': 'age_18_21',
                '21-24': 'age_21_24',
                '24-27': 'age_24_27',
                '27-30': 'age_27_30',
                '30-35': 'age_30_35',
                '35-45': 'age_35_45',
                '45-100': 'age_45',
            }
        }
        for response_field in ['sex','age']:
            if response.get(response_field):
                for item in response.get(response_field):
                    response[fields_map[response_field][item['value']]] = item['reach']

        import ipdb; ipdb.set_trace()
        super(PostStatistic, self).parse(response)
