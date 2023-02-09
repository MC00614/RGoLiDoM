t, r = [], []
for i in range(9) :
    i = list(map(int, input().split()))
    p = max(i)
    q = i.index(p)
    t.append(p)
    r.append(q)
u = t.index(max(t))
v = r[u]
print(max(t))
print(u+1, v + 1)