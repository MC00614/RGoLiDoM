# 1978

N = int(input())
Li = list(map(int, input().split()))
num= []
for i in Li :
    if i > 1 :
         cnt = 0
         for j in range(2, i) :
            if j > 1 :
                if i % j == 0 :
                    cnt+=1
         if cnt == 0 :
            num.append(i)
print(len(num))


                

