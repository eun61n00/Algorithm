# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 13305

import sys

input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

cost = 0
current_idx = 0
while True:
    if current_idx == N - 1:  # 끝까지 다 옴
        break
    next_idx = current_idx
    while prices[current_idx] <= prices[next_idx + 1]:  # 다음 도시보다 기름값이 작거나 같으면
        if next_idx == N - 2:
            break
        next_idx += 1  # 언제까지 작은지를 구해야함
    # next_idx 까지 지금 기름값으로 가기
    cost += (prices[current_idx] *
             sum(distances[current_idx:next_idx + 1]))
    current_idx = next_idx + 1

print(cost)
