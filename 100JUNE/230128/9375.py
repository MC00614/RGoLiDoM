import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    k = int(input())
    list1 = []
    list2 = []
    for i in range(k) :
        x, y = map(str, input().rstrip().split())
        list1.append(y)
    set_list1 = set(list1)
    for l in set_list1 :
        p = list1.count(l) #y의 종류별로  몇 번들어가졌는지 세줌
        list2.append(p)
    sum = 1
    for j in list2 :  
        sum*=j+1 #종류별 개수 + 안들어가는 경우(1)
    print(sum-1) #전체가 안들어간 경우는 없으므로 -1


    

    
        


