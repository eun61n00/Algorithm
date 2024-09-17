# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj_1260 DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for edge in graph:
    edge = edge.sort()

def dfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False for _ in range(n + 1)]
dfs(graph, v, visited)
print("")
visited = [False for _ in range(n + 1)]
bfs(graph, v, visited)
