# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11050 이항계수

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

factorial = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i

print(int(factorial[n] / (factorial[k] * factorial[n - k])))
