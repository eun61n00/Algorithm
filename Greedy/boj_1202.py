# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1202 보석 도둑

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewelries = []
bags = []
result = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelries, (m, v))

for _ in range(k):
    heapq.heappush(bags, int(input()))

result = [(0, 0) for _ in range(len(bags))]

print(jewelries)

for i in range(len(bags)):
    for m, v in jewelries:
        if m <= bags[i]:
            if v > result[i][1]:
                tmp = (result[i])
                result[i] = (m, v)
                heapq.heappop(jewelries)
                if tmp[0] != 0:
                    heapq.heappush(jewelries, tmp)
        else:
            break
        print("\t", result)

print(result)

print(sum([v for m, v in result]))