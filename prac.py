# !/usr/bin/env python
# -*- coding: utf8 -*-
# practice

def init(n):
    parent = [i for i in range(n + 1)]
    return parent

def find(x):
    global parent
    if parent[x] != x:
        return find(parent[x])
    else:
        return x

def union(x, y):
    global parent
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
        parent = [y if i == x else i for i in parent]
    else:
        parent[y] = x
        parent = [x if i == y else i for i in parent]

parent = init(6)
union(1, 2)
union(3, 4)
union(2, 3)
print(parent)

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 전체 노드에서 방문하지 않은 노드 중에서 start와 가장 가까운 노드를 반환
def get_closest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for v, c in graph[start]:
        distance[v] = c
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_closest_node()
        visited[now] = True
        # 현재 노드와 연결된 다르 노드 확인
        for v, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[v]:
                distance[v] = cost

def get_closest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index