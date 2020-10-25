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

@router.post("/items")
async def add_item(item: Item):
  print(33333333333)
  return {"message": "Item received"}
