# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 (나동빈, 한빛미디어) Ch7 이진 탐색
# 7-8.py 떡볶이 떡 만들기

# 떡의 개수(N)과 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split()))

# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += (x - mid)
    if total < m:
        end = mid - 1
    elif total > m:
        start = mid + 1
    else:
        break

print(mid)