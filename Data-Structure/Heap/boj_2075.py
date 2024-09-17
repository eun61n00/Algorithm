from sys import stdin
import heapq

# 5
# 12 7 9 15 5
# 13 8 11 19 6
# 21 10 26 31 16
# 48 14 28 35 25
# 52 20 32 41 49

n = int(stdin.readline())
min_heap = []
max_heap = [[-1000000000, 1000000000]]

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        heapq.heappush(min_heap, lst[j])

    while min_heap[0] < max_heap[0][1]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, heapq.heappop(max_heap)[1])

    for j in range(n):
        heapq.heappush(max_heap, [-min_heap[j], min_heap[j]])

min_heap = []
for i in range(n):
    heapq.heappush(min_heap, max_heap[i][1])

print(min_heap[0])

# lst = list(map(int, input().split))

