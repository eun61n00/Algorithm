#1665) get medium value
from sys import stdin
import heapq


n = int(stdin.readline())
left_heap = list() #max heap
right_heap = list() #min heap

for i in range(n):
    val = int(stdin.readline())
    if len(left_heap) == 0:
        heapq.heappush(left_heap, [-val, val])
    elif len(right_heap) == 0:
        heapq.heappush(right_heap, val)
    print(left_heap[0][1])