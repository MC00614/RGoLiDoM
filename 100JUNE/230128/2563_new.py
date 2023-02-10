n = int(input())
q= []
for i in range(n) :
    M, N = map(int, input().split())
    for x in range(10) :
        for y in range(10) :
            rec = [M+x, N+y], [M+x,N+y+1], [M+x+1,N+y], [M+x+1, N+y+1 ]
            q.append(rec)
tuple_arr = [tuple(p) for p in q]
print(len(set(tuple_arr)))


