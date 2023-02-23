import sys
input =  sys.stdin.readline
n = int(input())
list1 = []
for _ in range(n) :
    list1.append(int(input()))
list1.sort()
list3= []
for j in range(1, n) :
    list3.append(list1[j]-list1[j-1])
 
def GCDofTwoNumbers(a, b): 
    while b != 0 : 
        a, b = b, a%b 
    return a 
GCDarr = list3[0] 
for i in range(len(list3)): 
    GCDarr = GCDofTwoNumbers(GCDarr, list3[i])
new = []
for l in range(2,int(GCDarr**0.5)+1) :
    if GCDarr % l == 0 :
        new.append(l)
        if(l**2) != GCDarr :
            new.append(GCDarr//l)     
new.append(GCDarr)  
new.sort()
for q in new :
    print(q, end = ' ')

