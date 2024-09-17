# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2460 두 용액

import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

min = sys.maxsize
liquid.sort()
start = 0
end = n - 1
result = []

while start < end:
    mix = liquid[start] + liquid[end]

    if abs(mix) < min:
        min = abs(mix)
        result = [liquid[start], liquid[end]]

    if mix < 0:
        start += 1
    elif mix > 0:
        end -= 1
    else:
        break

print(*result)