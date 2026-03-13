#using mathematical formula
n = 5
res = ((n*(n+1))//2)**2
print(res)

#using brute force approach
n = 5
sum = 0
for i in range(1,n+1):
    res +=i**3
print(res)

#using genertaor expression
n = 5
res = sum(i**3 for i in range(1, n+1))
print(res)

#using enumarate list
n = 5
res = sum([i+1])**3 for i,_in enumerate(range(n))])
print(res)
