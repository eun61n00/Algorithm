# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 (나동빈, 한빛미디어) Ch7 이진 탐색
# 7-3.py 반복문으로 구현한 이진 탐색 소스

# 이진 탐색 소스코드 구현(반복문 이용)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None