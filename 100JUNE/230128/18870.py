
"""   시간초과 오류뜸 ㅠㅠ
import sys 
n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list2 = sorted(list1) 
list3 = []
for i in list1 :
    list3.append(list2.index(i))
for j in list3 :
    print(j, end = ' ')
list2 = list1.sort() 로 하면 오류가 뜨는데 왜 오류가 뜨는지 모르겠음
"""
