# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2003 수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

result = 0
sum = 0

# 첫번째 포인터
for i in range(n):
    # 두번째 포인터
    sum = seq[i]
    if sum == m:
        result += 1
        continue
    for j in range(i + 1, n):
        sum += seq[j]
        if sum == m:
            result += 1
            break

print(result)

start, end = 0, 0
result, sum = 0, 0

while start < n:
    sum = seq[start]
    while sum < m and end < n:
        sum += seq[end]
        end += 1
    if sum == m:
        result += 1
    start += 1
    end = start + 1

print(result)
