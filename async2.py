# -*- coding: utf-8 -*-
"""async.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pOZXYro3pXNPeWXYWGaqEN0IlYiecvtR
"""

import time
import asyncio

async def fetch_data(delay):
    print("data is fetched...")
    await asyncio.sleep(delay)
    print("data received...")
    return {"data":"some data"}

async def main(msg):
    print("start")
    task=fetch_data(2)
    result= await task
    print(f"data received: {result}")
    print("end")

obj_c=main("hello")
asyncio.run(obj_c)