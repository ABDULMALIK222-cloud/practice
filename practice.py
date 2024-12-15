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


# print the maximunm of array and minimum of array in the given arr as list print the maximum and minimum of given 5 integers by taking only 4 integers and return min and max of the list
import math
import re
import os
import random
import sys

def minmax(arr):
  arr.sort()
  sum=0
  for i in arr:
    sum += i
  print(sum - arr[4], sum - arr[0])

if__name__=="__main__:
  arr = list(map(input().rstrip().split()))
  minmax(arr)


