import sys
input = sys.stdin.readline
N, M = map(int, input().split())
list1, list2 = [], []
for i in range(N):
    i = input()
    list1.append(i)
for j in range(M):
    j = input()
    list2.append(j)
set_list1=set(list1)
cnt=0
for k in list2 :
    if k in set_list1:
        cnt+=1
print(cnt)
    