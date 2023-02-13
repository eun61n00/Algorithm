# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2805 나무 자르기

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in array:
        if tree > mid:
            total += (tree - mid)
    if total > m:
        start = mid + 1
    elif total < m:
        end = mid - 1
    else:
        break

print(mid)