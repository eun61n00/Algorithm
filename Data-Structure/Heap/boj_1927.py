import heapq
from sys import stdin

n = int(stdin.readline())
heap = list()
for _ in range(n):
    val = int(stdin.readline())
    if val == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, val)
