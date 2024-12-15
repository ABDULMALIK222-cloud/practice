import math
import re
import os
import random
import sys

def findMedian(arr):
  arr.sort()
  return arr[n//2]
if__name__=="__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  a = list(map(int, input().rstrip().split()))
  result = findMedian(arr)


# program based on the lonely integer except one number remaining elements in the array will be printed twice
import math
import re
import os 
import random
import sys

from collections import defaultdict

def lonelyinteger(a):
  count_dict = defaultdict(int)
  for i in a:
    count_dict[i]+=1
  for i in count_dict:
    if count_dict[i]==1:
      return i
if__name__=="__main__":
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    
