import sys



def recursion(s, l, r):
    global cnt  # global 해서 밖에서도 적용 되게 
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

input = sys.stdin.readline #줄바꿈을 포함함 \n
n = int(input())
for i in range(n) :
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt ) # 줄바꿈 지울라고 rstrip()
