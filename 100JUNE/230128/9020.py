m = 1
n = 10001

primes = set() 

a = [True for i in range(n)]

for i in range(2, int(n**0.5)+1):
    if a[i] == True:
        for j in range(2*i, n, i):
            a[j] = False

for i in range(m,n):
    if i>1 and a[i] == True:
        primes.add(i)  
T = int(input())
for k in range(T) :
    n = int(input())
    num= []
    x = []
    y = []
    if n//2 in primes :
        print(n//2, n//2)
        continue
    else :
        for t in primes :
            if t < n//2 :
                num.append(t)
        for l in num :
            if n - l in primes :
                x.append(l)
                y.append(n-l)
    print(x.pop(), y.pop())

    

             
        