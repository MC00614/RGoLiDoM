n = int(input())
for i in range(n) :
    M, N = map(int, input().split())
    q = []
    for x in range(10) :
        for y in range(10) :
            rec = [M+x, N+y], [M+x,N+y+1], [M+x+1,N+y], [M+x+1, N+y+1 ]
            q.append(rec)
    k = [x for x in k if x not in q]
print(10000-len(k))

