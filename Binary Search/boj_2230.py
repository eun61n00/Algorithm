# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2230 수 고르기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input().rstrip()))

array.sort()
result = sys.maxsize
start, end = 0, 0

while start < n and end < n:
    diff = array[end] - array[start]
    if diff < m:
        end += 1
    else:
        result = min(result, diff)
        start+= 1

print(result)


# ! 오답(왜 오답인지 모르겠음)
# while start <= end:
#     mid = (start + end) // 2
#     while mid <= end:
#         diff = array[mid] - array[start]
#         if diff < m:
#             mid += 1

#         elif diff > m:
#             if diff < result:
#                 result = diff
#                 mid -= 1
#             else:
#                 break

#         else:
#             result = diff
#             break
#     start += 1

