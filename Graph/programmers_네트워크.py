# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 네트워크


def solution(n, computers):
    visited = [False for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    answer = 0

    for i in range(len(computers)):
        for idx, val in enumerate(computers[i]):
            if i != idx and val == 1:
                graph[i + 1].append(idx + 1)

    def dfs(graph, v, visited):
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                dfs(graph, i, visited)

    for i in range(1, len(computers) + 1):
        if visited[i] == False:
            dfs(graph, i, visited)
            answer += 1

    return answer