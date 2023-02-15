# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 18352 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

# 도로 정보 입력받기
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)

queue = deque([(x, 0)])
visited[x] = True
while queue:
    v, cnt = queue.popleft()

    for i in graph[v]:
        if visited[i] == False:
            queue.append((i, cnt + 1))
            visited[i] = True
            distance[i] = cnt + 1

result = [idx for idx, d in enumerate(distance) if d == k]
if result:
    for i in result:
        print(i)
else:
    print(-1)