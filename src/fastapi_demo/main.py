#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-25 
"""
import uvicorn
import sys
from fastapi_demo import get_app

app=get_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9527)