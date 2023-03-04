# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 6988 타일 밟기

import sys

input = sys.stdin.readline

n = int(input().rstrip())
tiles = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = [tiles[x] - tiles[i] for x in range(n) if x > i]

print(graph)

result = []

# s는 tile 하나하나 다 들어감(index)
def dfs(graph, s, visited, val):
    visited.append(s)

    # dfs(graph, 2, [0], 5)
    if val in graph[s]:
        dfs(graph, graph[s].index(val), visited, val)
    else:
        return visited


for i in range(n):
    for j in range(len(graph[i])):
        visited = [i]
        visited = dfs(graph, j, visited, graph[i][j])
        if len(visited) > 2:
            print(visited)

# 11
# 1 2 6 7 11 12 13 15 17 20 23
# graph[0] - [1, 5, 6, 10, 11, 12, 14, 16, 19, 22]
# graph[2] - [1, 5, 6, ..]