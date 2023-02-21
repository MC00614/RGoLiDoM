import sys
input = sys.stdin.readline
n = int(input())
for i in range(n) :
    N, M = map(int, input().split())
    a = max(N, M)
    b = min(N, M)
    while b != 0 :
        r = a%b
        a = b
        b = r
    print(int(N*M/a))   


