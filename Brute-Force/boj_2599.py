# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1522 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

result = 0

for i in range(n - k):
    total = result
    
    if i == 0:
        result = sum(lst[i : i + k])
    else:
        total -= lst[i - 1]
        total += lst[i + k - 1]
        if total > result:
            result = total

print(result)