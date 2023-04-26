import sys
input = sys.stdin.readline
n = input()
list1= list(map(int, input().split()))
set_list1 =set(list1)
m = input()
list2= list(map(int, input().split()))
set_list2=set(list2)
dic1 = {}
for i in list2:
    if i in set_list1:
        dic1[i] = 1
    else:
        dic1[i] = 0
for j in list2:
    print(dic1[j], end= ' ')
    