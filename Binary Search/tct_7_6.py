# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 (나동빈, 한빛미디어) Ch7 이진 탐색
# 7-6.py 부품 찾기 답안 예시 (계수 정렬)

# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000000

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')