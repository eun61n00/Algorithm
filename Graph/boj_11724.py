# usr/bin/env python
# -*- coding: utf8 -*-
# boj 11724 연결 요소의 개수

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]

def dfs(graph, v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i)

answer = 0
for i in range(1, n + 1):
    if visited[i] == False:
        dfs(graph, i)
        answer += 1

print(answer)