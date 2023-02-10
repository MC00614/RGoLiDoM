import sys

n = int(sys.stdin.readline())
k = []
for i in range(n) :
    x, y = map(str, sys.stdin.readline().split())
    k.append((int(x), y, i))

k.sort(key=  lambda x : (x[0], x[2]) )

for j in range(n) :
    print(k[j][0], k[j][1])


 