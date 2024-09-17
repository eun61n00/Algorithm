# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2225 합분해

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]

for i in range(1, k + 1):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[n][k])