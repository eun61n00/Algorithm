# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1205 등수 구하기

import sys

input = sys.stdin.readline

N, new_point, P = map(int, input().split())
if N > 0:
    points = list(map(int, input().split()))
else:
    print(1)
    exit()
if N == P and new_point <= points[-1]:
    print(-1)
    exit(0)

points.append(new_point)
points.sort(reverse=True)
before_point = points[0]
rank = [1]
for idx, point in enumerate(points[1:]):
    if before_point == point:
        rank.append(rank[-1])
    else:
        rank.append(idx + 2)
    before_point = point

# print(f"points: {points}")
# print(f"rank: {rank}")
print(rank[points.index(new_point)])
