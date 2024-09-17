# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 10844 쉬운 계단 수

import sys
input = sys.stdin.readline

n = int(input().strip())
stairs = [[1 for _ in range(10)] for __ in range(n + 1)]
stairs[1][0] = 0

for i in range(2, n + 1):
    for j in range(10):
        if j - 1 < 0:
            stairs[i][j] = stairs[i - 1][j + 1] % 1000000000
        elif j + 1 > 9:
            stairs[i][j] = stairs[i - 1][j - 1] % 1000000000
        else:
            stairs[i][j] = (stairs[i - 1][j - 1] + stairs[i - 1][j + 1]) % 1000000000

print(sum(stairs[n]) % 1000000000)