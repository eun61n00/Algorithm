# -*- coding: utf-8 -*-
# boj 2747 피보나치 수

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 46
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])

# -*- coding: utf-8 -*-
# boj 2747 피보나치 수
# Time OUT***

input = sys.stdin.readline

n = int(input())


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(n))

# -*- coding: utf-8 -*-
# boj 2747 피보나치 수
# 재귀 함수아닌 단순 반복문으로 풀이

input = sys.stdin.readline

n = int(input())
a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)
