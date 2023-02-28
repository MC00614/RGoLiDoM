import sys
input = sys.stdin.readline
n , k = map(int, input().split())
s = []
for i in range(1,int(n**0.5)+1) :
    if n%i == 0 :
        s.append(i)
        if i**2 !=n :
            s.append(n//i)
s.sort()
if k <= len(s) :
    print(s[k-1])
else :
    print(0)