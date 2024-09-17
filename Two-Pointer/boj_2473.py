# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2460 세 용액

import sys

input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))

result = []
min = sys.maxsize
start = 1
end = n - 1

for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        mix = liquid[i] + liquid[start] + liquid[end]
        if abs(mix) < min:
            min = abs(mix)
            result = [liquid[i], liquid[start], liquid[end]]

        if mix < 0:
            start += 1
        elif mix > 0:
            end -= 1
        else:
            exit()

print(*result)