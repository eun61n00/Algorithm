# usr/bin/env python
# -*- coding: utf8 -*-
# 이것이 코딩 테스트다 Ch11 Q04 만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

answer = 0
for i in range(1, sum(coins) + 1):
    remain = i
    for coin in coins:
        if coin <= remain:
            remain -= coin
            if remain == 0: # 해당 금액 만들어짐
                break
    if remain > 0: # 모든 동전을 사용했지만 만들어지지 않음
        answer = i
        break

if answer == 0:
    answer = sum(coins) + 1

print(answer)

# 교재 답안 예시

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 # 금액 1을 만들 수 있는 지 확인
for x in data:
    if target < x: # 만들 수 없는 금액을 찾았을 때 종료
        break
    target += x

print(target)