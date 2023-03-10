# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다(나동빈, 한빛미디어)
# 6-3.py 삽입 정렬 소스코드

array = list(map(int, input().split()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
