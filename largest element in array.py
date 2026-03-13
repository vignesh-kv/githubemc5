#using built-in max() function
arr = [10,324,45,90,208]
res = max(arr)
print(res)

#using iteration
arr = [10,324,45,90,208]
res = arr[0]
for i in range(1, len(arr)):
    if arr[i] > res:
        res = arr[i]
print(res)

#using reduce()function
from functools import reduce
arr = [10,324,45,90,9808]
res = reduce(max, arr)
print(res)

#using sort()fuction
arr = [10,324,45,90,9808]
arr.sort()
res = arr[-1]
print(res)

#using operator.gt()
import operator
arr = [2,1,7,3,0]
res = 0
for i in arr:
    if operator.gt(i,res):
        res = i
print(res)
