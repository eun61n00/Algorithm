# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 단어 변환

from collections import deque

def solution(begin, target, words):
    answer = []

    graph = [[] for _ in range(len(words))]
    start = []

    if target not in words:
        return 0

    def bfs(graph, s):
        queue = deque()
        visited = [False for _ in range(len(words))]
        queue.append((s, 1))
        visited[s] = True

        while queue:
            v, step = queue.popleft()
            if words[v] == target:
                return step
            for i in graph[v]:
                if visited[i] == False:
                    queue.append((i, step + 1))
                    visited[i] = True

    # 해당 단어에서 갈 수 있는 단어 정보 저장 (그래프 만들기)
    for i in range(len(words)):
        word1 = words[i]
        for j in range(len(words) - i - 1):
            word2 = words[i + j + 1]
            if len([ch for idx, ch in enumerate(word2) if ch != word1[idx]]) == 1:
                graph[i].append(i + j + 1)
                graph[i + j + 1].append(i)

        if len([ch for idx, ch in enumerate(begin) if ch != word1[idx]]) == 1:
            start.append(i)

    for s in start:
        answer.append(bfs(graph, s))

    if min(answer) == None:
        return 0
    return min(answer)