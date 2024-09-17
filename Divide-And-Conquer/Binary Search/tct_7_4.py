# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 (나동빈, 한빛미디어) Ch7 이진 탐색
# 7-4.py 부품 찾기

import sys

input = sys.stdin.readline

n = int(input().rstrip())
components = sorted(list(map(int, input().split())))
m = int(input().rstrip())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

result = []
for component in request:
    if binary_search(components, component, 0, n) == None:
        result.append("no")
    else:
        result.append("yes")

print(*result)


# 답안 예시
# N(가게의 부품 개수 입력)
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# ㅡ