# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj_2606 바이러스

import sys

input = sys.stdin.readline

computer_cnt = int(input())
network_cnt = int(input())

graph = [[] for _ in range(computer_cnt + 1)]
visited = [False for _ in range(computer_cnt + 1)]

for _ in range(network_cnt):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 1번 컴퓨터에 연결되어있는 컴퓨터 개수 출력 (dfs - 1번에서 가장 깊은 곳까지 탐색)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(True) - 1)