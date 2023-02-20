import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
set_k = set()
set_k.add(x)
set_k.add(y)
set_k.add(w-x)
set_k.add(h-y)
print(min(set_k))

