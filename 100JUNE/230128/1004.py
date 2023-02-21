import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    x1, y1, x2, y2 = map(int, input().split())
    planet = int(input())
    list1 = []
    list2, list3 = [], []
    for j in range(planet) :
        x, y, r = map(int, input().split())
        d1 = (x1-x)**2 +(y1-y)**2
        d2 = (x2-x)**2 +(y2-y)**2
        d1 = d1**0.5
        d2 = d2**0.5
        if d1 < r :
            list2.append((x,y,r))
        if d2 < r :
            list3.append((x,y,r))
    list2 = set(list2)
    list3 = set(list3)
    list4 = list(list2 ^ list3)
    print(len(list4))    
    

