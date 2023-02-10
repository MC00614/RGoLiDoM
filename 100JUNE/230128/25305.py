N, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = sorted(list1)
print(list2[N-k])
