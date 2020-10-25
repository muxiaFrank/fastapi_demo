#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
class BaseConfig(object):
    CELERY_BROKER_URL = 'redis://0.0.0.0:6379/2'
    CELERY_RESULT_BACKEND = 'redis://0.0.0.0:6379/3'
    CELERY_TASK_SERIALIZER = 'json'