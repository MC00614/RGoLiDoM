import  sys
input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
        continue
    else :
        d = (x1-x2)**2 + (y1-y2)**2
        d = d**0.5
        R = max(r1,r2)
        r = min(r1, r2)
        if d < R :
            if d < R - r :
                print(2)
            elif d == R - r :
                print(1)
            else :
                print(0)
        else :
            if d > R + r :
                print(0)
            elif d ==R + r :
                print(1)
            else :
                print(2)

    
