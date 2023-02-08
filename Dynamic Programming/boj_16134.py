# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 16134 조합(Combination)

import sys
input = sys.stdin.readline

n, r = map(int, input().split())
factorial = [1 for _ in range(n + 1)]
div = 1000000007

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    x = power(base, exponent // 2)
    if exponent % 2:
        return x * x * base % div
    else:
        return x * x % div

for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i

print(int(factorial[i] * power(factorial[r] * factorial[n - r], div - 2) % div))