# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 12852 1로 만들기 2

n = int(input())

dp = [0] * (n + 1)
dp[1] = 0

dp2 = [0] * (n + 1)

for i in range(2, n + 1):
    answer = []
    dp[i] = dp[i - 1] + 1
    dp2[i] = i - 1
    if i % 2 == 0:
        if dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
            dp2[i] = i//2
        dp[i] = min(dp[i//2] + 1, dp[i])
    if i % 3 == 0:
        if dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            dp2[i] = i//3

print(dp[n])
print(n, end=" ")
while n > 1:
    print(dp2[n], end=" ")
    n = dp2[n]
