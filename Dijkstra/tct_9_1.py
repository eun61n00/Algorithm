# 이것이 코딩 테스트다 9-1.py
# 간단한 다익스트라 알고리즘 소스코드

import sys
input = sys.stdin.readline
INF = int(1e9)									# 무한을의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 오드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
# (n+1의 크기로 만들어 노드의 번호를 인덱스로 바로 접근할 수 있도록 함)
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
	u, v, w = map(int, input().split()) 		# u: 시작 노드, v: 끝 노드, w: 가중치 (u번 노드에서 b번 노드로 가는 비용이 w)
	graph[u].append((v, w))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_closest_node():
	min_value = INF
	index = 0 									# 가장 최단 거리가 짧은 노드(index)
	for i in range(1, n + 1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index

def dijkstra(start):
	distance[start] = 0							# 시작 노드에 대해서 초기화
	visited[start] = True

	for j in graph[start]:
		distance[j[0]] = j[1]
	# 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
	for i in range(n-1):
		# 현재 최단 거리가 가장 짧은 노드에 방문
		now = get_closest_node()
		visited[now] = True
		# 현재 노드와 연결된 다른 노드 확인
		for j in graph[now]:
			cost = distance[now] + j[1]
			# 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[j[0]]:
				distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra()

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
	# 도달할 수 없는 경우, INF 출력
	if distance[i] == INF:
		print("INF")
	else:
		print(distance[i])
