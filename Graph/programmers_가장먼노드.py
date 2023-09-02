# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 프로그래머스 가장 먼 노드

import heapq

INF = int(1e9)

def solution(n, edge):

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    # 간선 정보 저장하기(graph 만들기)
    for e in edge:
        a, b = e[0], e[1]
        graph[a].append(b)
        graph[b].append(a)

    queue = []

    def dijkstra(start):
        distance[start] = 0
        heapq.heappush(queue, (0, start))
        while queue:
            dist, current = heapq.heappop(queue)
            if distance[current] < dist:
                continue
            for e in graph[current]:
                cost = dist + 1
                if cost < distance[e]:
                    distance[e] = cost
                    heapq.heappush(queue, (cost, e))

    dijkstra(1)
    max_distance = max(distance[1:])
    return distance.count(max_distance)
