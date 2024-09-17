# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11000 강의실 배정

import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
class_times = [list(map(int, input().split())) for _ in range(n)]
class_times.sort(key=lambda x: x[0])

queue = []
for time in class_times:
    # queue[0]: 현재 진행 중인 강의 중에 가장 빨리 끝나는 강의 시간
    if queue and queue[0] <= time[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, time[1])

print(len(queue))
