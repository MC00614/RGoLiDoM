import sys
from collections import Counter
input = sys.stdin.readline
list1 =  []
list2 =  []
list3 =  []
for _ in range(3) :
    x, y = map(int, input().split())
    list1.append(x)
    list2.append(y)
for i in list1:
    if list1.count(i) == 1 :
        list3.append(i)
        break
for j in list2:
    if list2.count(j) == 1 :
        list3.append(j)
        break
for k in list3:
    print(k, end= '')




