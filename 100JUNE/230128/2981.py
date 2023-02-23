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
    j = j - list1[0]    #가장 작은 수를 리스트에서 다빼줬음
    list3.append(j)
 
def GCDofTwoNumbers(a, b): #GCDofTwoNumbers라는 이름의 함수와 매개변수 a, b 정의하기
    while b != 0 : #b가 0이 아닌 동안 반복
        a, b = b, a%b #a에 b를, b에 a와 b를 나눈 나머지를 교환하여 저장(스왑)
    return a #반환되는 a가 두 수의 최대공약수
 
GCDarr = list3[0] #arr 리스트의 첫 번째 항목(0번 방)을 GCDarr에 저장
for i in range(len(list3)): # i가 0부터 리스트 arr의 길이만큼 반복
    GCDarr = GCDofTwoNumbers(GCDarr, list3[i]) # GCDarr에 GCDarr과 arr[i]의 최대공약수를 저장
list4 = []    
for l in range(2,GCDarr+1) :
    if GCDarr % l == 0 :
        print(l, end= ' ')
