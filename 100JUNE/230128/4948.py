m = 123456
num = []
for i in range(2*m + 1) :
    if i > 1:
        for j in range(2, int(i**0.5)+1) :
            if i % j == 0 :
               break
        else :
            num.append(i)
while True :
    n= int(input())
    cnt = 0
    if n == 0 :
        break
    else :
        for k in num :
            if n < k < 2*n + 1 :
               cnt +=1
        print(cnt)
        
            
