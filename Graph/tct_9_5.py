# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩테스트다 9-3.py
# 실전 문제 전보

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 입력 받기
n, m, c = map(int, input().split())
durations = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
queue = []
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
print(graph)
def dijkstra(start):
    heapq.heappush(queue, (0, start))
    durations[start] = 0
    while queue:
        duration, current_city = heapq.heappop(queue)
        if durations[current_city] < duration:
            continue
        for edge in graph[current_city]: # 해당 노드 방문
            c = duration + edge[1] # 해당 노드까지의 거리와 해당 노드에서 이어진 노드가지의 거리: c
            if c < durations[edge[0]]:
                durations[edge[0]] = c
                heapq.heappush(queue, (c, edge[0]))
                print("heappush")

# 정답 출력
print(n - durations.count(INF), end=" ") # 메시지를 받는 도시의 총 개수
print(max([time for time in durations if time < INF])) # 걸리는 시간


# 예시 답안
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for edge in graph[now]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(queue, (cost, edge[0]))

dijkstra(start)

count = 0   # 도달할 수 있는 노드의 개수
max_distance = 0    # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)