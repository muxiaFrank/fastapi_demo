#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
from fastapi import APIRouter

router = APIRouter()
from fastapi_demo.items.demo_items import Item

from fastapi_demo.tasks.task import process_item
from fastapi_demo.core.celery_app import celery_app

@router.post("/items")
async def add_item(item: Item):
  process_item.delay(1,2,3.33)

  return {"message": "Item received"}
