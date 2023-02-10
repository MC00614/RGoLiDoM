N = int(input())
set_A = set()
for i in range(N) :
    set_A.add(int(input()))
set_B = sorted(set_A)
for j in set_B :
    print(j)
