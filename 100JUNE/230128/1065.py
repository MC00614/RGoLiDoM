N = int(input())
cnt = 0
for i in range(1, N+1) :
    if i < 100 :
        cnt+=1
    else :
        k = list(map(int, str(i)))
        if k[0] + k[2] == 2 * k[1] :
            cnt+=1
print(cnt)



