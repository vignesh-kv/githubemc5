#using sieve of eratosthenes
x,y = 2,11
prime = [True]*(y+1)
primes[0], primes[1] = false,false
for i in range(2, int(y**0.5)+1):
    if primes[i]:
        for j in range(i*i,y+1,i)
        prime[j] = false
res = [i for i in range(x,y+1)
       ifprimes[i]]
print(res if res else "no")

#using navie approach
x,y = 2,7
res = []
for i in range(x,y+1):
    if i <=1:
        continue
    for j in range(2,i//2+1):
        if i%j == 0
        break
    else:
        res.append(i)
print(res if res else "no")
