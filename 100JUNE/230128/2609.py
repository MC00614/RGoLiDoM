import sys
input =  sys.stdin.readline
N, M = map(int, input().split())

i = 2
list2=[]
while i <= min(M, N) :
    if M%i == 0 and N%i == 0 :
        M = M/i
        N = N/i
        list2.append(i)
        i=2
    else :
        i+=1
sum = 1
for j in list2:
    sum*=j
print(sum, int(sum*M*N))