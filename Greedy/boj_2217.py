# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2217 로프

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

max_weights = 0
tmp = n
while tmp > 0:
    # n개의 로프를 사용할 때 최대 들어올릴 수 있는 무게
    max_weights = max(tmp * ropes[n - tmp], max_weights)
    tmp -= 1

print(max_weights)
