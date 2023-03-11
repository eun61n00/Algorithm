# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다(나동빈, 한빛미디어)
# 6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(list(map(int, input().split()))))