#using sum()function
arr = [12,3,4,15]
ans = sum(arr)
print('sum:',ans)

#using reduce()method
from functools import reduce
arr = [12,3,4,15]
ans = reduce(lambda a,b:a+b,arr)
print('sum:',ans)

#using iteration
arr = [12,3,4,15]
t = 0
for x in arr:
    t += x
print('sum:',t)

#using enumerate()function
arr = [12,3,4,15]
t = 0
for i,val in enumerate(arr):
    t += val
print(t)
