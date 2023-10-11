# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14501 퇴사

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    t, p = map(int, input().split())
    meetings.append((t, p))


# BFS 풀이
def bfs(x):
    if x + meetings[x][0] > n:
        return 0
    max_revenue = meetings[x][1]
    revenue = meetings[x][1]
    queue = deque([(x, revenue)])

    while queue:
        current, revenue = queue.popleft()
        max_revenue = max(revenue, max_revenue)
        for i in graph[current]:
            queue.append((i, revenue + meetings[i][1]))

    return max_revenue


graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + meetings[i][0], n):
        if j + meetings[j][0] <= n:
            graph[i].append(j)

revenues = []
for i in range(n):
    revenues.append(bfs(i))

print(max(revenues))


# DP 풀이
dp = [0 for _ in range(n + 1)]

for i in range(n):  # i일까지 일했을 때 최대 수익
    for j in range(i + meetings[i][0], n + 1):  # i일 상담 진행했을 때 상담 가능한 날부터 돌기
        dp[j] = max(dp[j], dp[i] + meetings[i][1])

print(dp[-1])
