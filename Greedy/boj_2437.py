# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2437 저울

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input().rstrip())
weights = list(map(int, input().split()))
weights.sort()

num = 1
for i in range(n):
    if num < weights[i]:
        break
    num += weights[i]
print(num)
