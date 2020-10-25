#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
from fastapi_demo.core.celery_app import celery_app
from celery import current_task
import time

@celery_app.task(acks_late=True)
def process_item(id: int,quantity: int, price: float) -> str:
    # for i in range(1, 11):
    time.sleep(10)
    current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': 10})
    print(6666666)

    return f"finished processing item: {id} | {quantity} | {price}"