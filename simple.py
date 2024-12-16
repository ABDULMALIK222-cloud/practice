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
# program to swap the elements first element to last element
def interchange(list):
  size = len(list)
  temp = list[0]
  list[0] = list[size -1]
  list[size -1] = temp
  return list

#driver code
list = [1,2,3,4,5,6]
print(interchange(list))

# using tuple variable swappint hte first and last element in a list
def interchange(list):
  #storing first and last elements of list using get tuple variable
  get = list[0],list[-1]
  #swapping the variables
  list[0],list[-1] = get
  return list

#driver code
list = [1,2,3,4,5]
print(interchange(list))

#using  * operand swapping the elements
def interchage(list):
  start,*middle,end = list
  list =[end,*middle,start]
  return list

#driver code
list = [1,2,3,4,5]
print(interchange(list))
# program to slice the elements in the list
def interchange(list):
  #check if 2 elements are present in it or not
  if(len(list))>2:
    list = list[-1:] + list[1:-1]+list[:1]
  return list
#driver code
list = [1,2,3,4,5]
print(interchange(list))
    
