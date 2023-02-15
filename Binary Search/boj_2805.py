# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2805 나무 자르기

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in array:
        if tree > mid:
            total += (tree - mid)

    if total > m:
        start = mid + 1
        result = mid
    elif total < m:
        end = mid - 1
    else:
        result = mid
        break

print(result)