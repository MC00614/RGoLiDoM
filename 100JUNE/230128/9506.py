import sys
input = sys. stdin.readline

while True :
    s = []
    n = int(input())
    if n == -1 :
        break 
    for i in range(1,int(n**0.5)+1) :
        if n%i == 0 :
            s.append(i)
            if i**2 !=n :
                s.append(n//i)
    s.sort()
    s.pop()
    if sum(s) == n :
        print(n , end= ' = ')
        p = s[-1]
        s.pop()
        for l in s :
            print(l, end= ' + ')
        print(p)
    else :
        print(f"{n} is NOT perfect")
