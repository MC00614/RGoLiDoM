N= int(input())
cnt= 0
for j in range(N) :
    k = input()
    k=list(k)
    q = list(set(k))
    new = []
    new.append(k[0])
    i = 0
    while i < len(k) - 1 :
        if k[i] != k[i+1] :
            new.append(k[i+1])
        i+=1
    if len(q) == len(new) :
        cnt+= 1
print(cnt)
