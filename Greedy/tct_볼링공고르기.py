# usr/bin/env python
# -*- coding: utf8 -*-
# 이것이 코딩 테스트다 Ch11 Q05 볼링공 고르기

from collections import Counter

n, m = map(int, input().split())
balls = list(map(int, input().split()))
counter = Counter(balls)

answer = (n * (n - 1)) // 2
for key, value in counter.items():
    if value  > 1:
        answer -= (value * (value - 1)) // 2

print(answer)


# 교재 답안 예시(A05.py)
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1   # 각 무게에 해당하는 볼링공의 개수 카운트

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기(같은 무게라도 서로 다른 볼링공으로 취급하므로)

print(result)