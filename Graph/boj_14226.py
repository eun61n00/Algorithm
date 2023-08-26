# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14226 이모티콘

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
result = 0

graph = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
graph[1][0] = 0
queue = deque([(1, 0)])

while queue:
    s, c = queue.popleft()

    # 복사하기
    if graph[s][s] == 0:
        graph[s][s] = graph[s][c] + 1
        queue.append((s, s))

    # 붙여넣기
    if s + c <= n and graph[s + c][c] == 0:
        graph[s + c][c] = graph[s][c] + 1
        queue.append((s + c, c))

    # 삭제하기
    if s > 0 and graph[s - 1][c] == 0:
        graph[s - 1][c] = graph[s][c] + 1
        queue.append((s - 1, c))

print(min([i for i in graph[n] if i != 0]))

n = int(input().strip())
clipboard = 1
cnt = 2
result = 0
dp = [0 for _ in range(n + 1)]
dp[2] = 2

if n % 2 == 0:
    while cnt == n // 2:
        dp[cnt]
        cnt += 1

while cnt != n:

    # 기존 클립보드 붙여넣기
    if dp[cnt] + clipboard == n:
        result += 1
        cnt += clipboard
        dp[cnt] += clipboard
        continue

    # 복사 후 + 붙여넣기
    if dp[cnt] + clipboard < n:
        clipboard = dp[cnt] # 클립보드 덮어쓰기 (복사 수행)
        cnt += clipboard # 붙여넣기 수행
        result += 2 # 연산 시간 더하기 (복사 + 붙여넣기 = 2초)
        dp[cnt] = result
        continue

print(result)