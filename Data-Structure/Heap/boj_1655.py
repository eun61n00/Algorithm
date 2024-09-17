from sys import stdin
import heapq


n = int(stdin.readline())
left_heap = list()  # max heap
right_heap = list()  # min heap

for i in range(n):
    val = int(stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, [-val, val])
    else:
        heapq.heappush(right_heap, val)

    if right_heap and left_heap[0][1] > right_heap[0]:
        left_popped_val = heapq.heappop(left_heap)[1]
        right_popped_val = heapq.heappop(right_heap)
        heapq.heappush(left_heap, [-right_popped_val, right_popped_val])
        heapq.heappush(right_heap, left_popped_val)

    # if i == 0:
    #     heapq.heappush(left_heap, [-val, val])
    # elif i == 1:
    #     if val >= left_heap[0][1]:
    #         heapq.heappush(right_heap, val)
    #     else:
    #         popped_value = heapq.heappop(left_heap)[1]
    #         heapq.heappush(right_heap, popped_value)
    #         heapq.heappush(left_heap, [-val, val])
    # else:
    #     if val >= right_heap[0]:  # when input value is bigger than current medium value
    #         if len(right_heap) - len(left_heap) == -1:
    #             heapq.heappush(right_heap, val)
    #         else:
    #             popped_value = heapq.heappop(right_heap)
    #             heapq.heappush(left_heap, [-popped_value, popped_value])
    #             heapq.heappush(right_heap, val)
    #     else:  # when input value is smaller than current medium value
    #         if len(left_heap) - len(right_heap) == 0:
    #             heapq.heappush(left_heap, [-val, val])
    #         else:
    #             popped_value = heapq.heappop(left_heap)[1]
    #             heapq.heappush(right_heap, popped_value)
    #             heapq.heappush(left_heap, [-val, val])

    print(left_heap[0][1])
