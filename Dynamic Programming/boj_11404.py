# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11404 플로이드

import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수(n)과 버스 개수(m)
n = int(input())
m = int(input())

# 2차원 리스트(그래프) 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 버스 비용 정보 입력받기
for _ in range(m):
    start, end, cost = map(int, input().split())
    if graph[start][end] != 0 and graph[start][end] != INF:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost


# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            graph[a][b] = 0
        if b == n:
            print(graph[a][b], end="\n")
        else:
            print(graph[a][b], end=" ")