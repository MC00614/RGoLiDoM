import sys
input =sys.stdin.readline
n = int(input())
list1= list(map(int, input().split()))
list1.sort()
if len(list1) > 1 :
    print(list1[0]*list1[-1])
else :
    print(list1[0]**2)
    