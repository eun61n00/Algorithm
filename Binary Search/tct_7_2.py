# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 (나동빈, 한빛미디어) Ch7 이진 탐색
# 7-2.py 재귀 함수로 구현한 이진 탐색 소스

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
