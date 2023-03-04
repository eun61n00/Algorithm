# usr/bin/env python
# -*- coding: utf8 -*-
# 이것이 코딩 테스트다 Ch11 Q01 모험가 길드

n = int(input())
fear_score = list(map(int, input().split()))
fear_score.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in fear_score: # 낮은 공포도부터 확인
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        result += 1
        count = 0

print(result)