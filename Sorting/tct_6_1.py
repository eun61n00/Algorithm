# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다(나동빈, 한빛미디어)
# 6-1.py 선택 정렬 소스코드

array = list(map(int, input().split()))

for i in range(len(array)):
    # 가장 작은 원소의 인덱스 -> 차례로 정렬
    min_index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
