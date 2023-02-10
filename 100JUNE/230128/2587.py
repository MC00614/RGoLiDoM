list1 = []
for i in range(5) :
    list1.append(int(input()))
list2 = sorted(list1)
print(sum(list2)//5)
print(list2[2])
