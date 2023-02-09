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

visited = [False for _ in range(n + 1)]

def dfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    visited[v] = True
    queue.append(*graph[v])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        if visited[v] =

dfs(graph, v, visited)