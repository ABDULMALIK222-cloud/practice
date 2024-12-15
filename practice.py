# probability of number of positive and negative and zeros as their occurence in the list from the list and return the probabiliity of the numbers 
import math
import re
import os
import random
import sys

def plusminus(arr):
  p = 0
  m = 0
  l = 0
  for i in arr:
    if int(i) > 0:
      p += 1
    if int(1 < 0:
      m += 1
    if int(i) == 0:
      l += 1
  print(p/n)
  print(m/n)
  print(l/n)
if__name__=="__main__:
  n = int(input().strip())
  arr = list(map(input().strip().split()))
  plusminus(arr)
      
