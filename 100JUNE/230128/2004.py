import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2  # n!에 포함된 2의 개수를 세줌
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5 #n!에 포함된 5의 개수를 세줌
        five += n
    return five
print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))