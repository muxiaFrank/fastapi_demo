#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
from fastapi import APIRouter

from fastapi_demo.api.v1.demo import router as router_item

router = APIRouter()

router.include_router(router_item, tags=["v1"], prefix="/v1")
