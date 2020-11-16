#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
from fastapi_demo.core.config import BaseConfig

import os
from time import sleep
from celery import Celery, current_task

celery_app = Celery(
    "worker",
    broker=BaseConfig.CELERY_BROKER_URL,
    include=['fastapi_demo.tasks.task']
)
celery_app.conf.task_routes = {
    "fastapi-demo.worker.celery_worker.queue": "items"}

celery_app.conf.update(task_track_started=True)