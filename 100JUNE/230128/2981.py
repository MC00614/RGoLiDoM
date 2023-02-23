import sys
input =  sys.stdin.readline
n = int(input())
list1 = []
for _ in range(n) :
    list1.append(int(input()))
list1.sort()
list2 = list1[1:]
list3= []
for j in list2 :
    j = j - list1[0]    
    list3.append(j)
 
def GCDofTwoNumbers(a, b): 
    while b != 0 : 
        a, b = b, a%b 
    return a 
 
GCDarr = list3[0] 
for i in range(len(list3)): 
    GCDarr = GCDofTwoNumbers(GCDarr, list3[i])
for l in range(2,GCDarr+1) :
    if GCDarr % l == 0 :
        print(l, end= ' ')
