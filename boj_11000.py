# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11000 강의실 배정

import sys
input = sys.stdin.readline

n = int(input().rstrip())
classes = [list(map(int, input().split())) for _ in range(n)]

# 시간초과
# rooms = []
# for start, end in classes:

#     complete = False
#     if len(rooms) == 0:
#         rooms.append([1 if time in range(start, end) else 0 for time in range(end)])
#         continue

#     for room in rooms:
#         if 1 in room[start:end]:        # 수업이 있는 시간이 있으면
#             continue
#         else:
#             room[start : end] = [1 for _ in range(start, end)]
#             complete = True
#             break
#     if not complete:
#         rooms.append([1 if time in range(start, end) else 0 for time in range(end)])

# print(len(rooms))

# 정렬 후, 우선순위 큐 사용
import heapq
classes.sort(key=lambda x: x[0])

heap = []