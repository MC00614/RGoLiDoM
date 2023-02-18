import sys
input = sys.stdin.readline
n = int(input())
p = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                t = str(i)+str(j)+str(666)+str(k)+str(l)
                x = str(i)+str(666)+str(k)+str(l)+str(j)
                y = str(666)+str(k)+str(l)+str(i)+str(j)
                z = str(k)+str(l)+str(i)+str(j)+str(666)
                u = str(l)+str(i)+str(j)+str(666)+str(k)
                p.append(int(t))
                p.append(int(x))
                p.append(int(y))
                p.append(int(z))
                p.append(int(u))                
set_p =set(p)
a = list(set_p)
a.sort()
print(a[n-1])
