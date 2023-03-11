# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다(나동빈, 한빛미디어)
# 6-4.py 퀵 정렬 소스코드

array = list(map(int, input().split()))

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종룔
    if start == end:
        return

    # pivot은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # pivot 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

def quick_sort(array, start, end):

    # 쪼개고 쪼개다가 원소가 하나가 되면 그냥 return(재귀 종료)
    if start == end:
        return

    pivot = 0
    left = start + 1
    right = end
    while left <= right:
        # pivot 보다 큰 수를 찾을 때까지 left를 오른쪽으로 한 칸 이동시키기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot 보다 작은 수를 찾을 때까지 right를 왼쪽으로 한 칸 이동시키기
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

