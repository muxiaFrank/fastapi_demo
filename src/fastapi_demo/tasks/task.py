#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
from fastapi_demo.core.celery_app import celery_app
from celery import current_task
import time


def get_expection():
    print("start")
    time.sleep(5)
    raise Exception("this is a demo")

@celery_app.task(acks_late=True)
def process_item(id: int,quantity: int, price: float) -> str:
    # for i in range(1, 11):
    current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': 10})
    try:
        get_expection()
    except Exception as e:
        print(11111)
        print(e)

    return f"finished processing item: {id} | {quantity} | {price}"

