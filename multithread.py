# -*- coding: utf-8 -*-
"""Multithread.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hHqlzDZJBL9AXM1lELEIVrhikTzgY4Yk
"""

import time
import threading

def square(num_list):
  for n in numList:
    time.sleep(0.3)
    print("square",n*n)

def cube(num_list):
  for n in numList:
    time.sleep(0.3)
    print("cube",n*n*n)

numList = [1,2,3,4,5,6]

t=time.time()
square(numList)
cube(numList)
print("job finished...(No threading)",time.time()-t)

t=time.time()
t1=threading.Thread(target=square,args=(numList,))
t2=threading.Thread(target=cube,args=(numList,))

t1.start()
t2.start()

t1.join()
t2.join()

print("job finished...(threading)",time.time()-t)