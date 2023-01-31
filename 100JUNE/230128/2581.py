M = int(input())
N = int(input())
num = []
for i in range(M, N+1) :
    cnt= 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
             cnt+=1
        if cnt == 0 :
            num.append(i)
if len(num) < 1 :
    print(-1)
else :    
    print(sum(num))
    print(num[0])