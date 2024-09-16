# -*- coding: utf-8 -*-
"""async.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pOZXYro3pXNPeWXYWGaqEN0IlYiecvtR
"""
#async example
import time
import asyncio

async def main(msg):
    print("start")
    await asyncio.sleep(1)
    print(msg)

obj_c=main("hello")
asyncio.run(obj_c)