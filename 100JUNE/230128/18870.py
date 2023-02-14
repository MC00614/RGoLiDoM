
"""   시간초과 오류뜸 ㅠㅠ
import sys 
n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list2 = sorted(list1) 
list3 = []
for i in list1 :
    list3.append(list2.index(i)) 인덱스라 시간초과 오류가 뜨는듯>
for j in list3 :
    print(j, end = ' ')
list2 = list1.sort() 로 하면 오류가 뜨는데 왜 오류가 뜨는지 모르겠음
"""

import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int, input().split()))
list2 = list(sorted(set(list1))) # 정렬하고 리스트화 dic에 집어넣기
dic = {list2[i]:i for i in range (len(list2))}

for i in list1  :
    print(dic[i], end= ' ')