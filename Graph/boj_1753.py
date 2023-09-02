# boj_1753
# https://www.acmicpc.net/problem/1753

# 이것이 코딩테스트다 9-2.py
# 개선된 다익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q: # 큐가 비어있지 않다면
		dist, current = heapq.heappop(q)
		if distance[current] < dist:
			continue	# 현재 노드가 이미 처리된 적이 있는 노드라면 무시

		for i in graph[current]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
	if distance[i] == INF:
		print("INF")
	else:
		print(distance[i])