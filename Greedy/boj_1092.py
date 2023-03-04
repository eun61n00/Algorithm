# usr/bin/env python
# -*- coding: utf8 -*-
# boj 1092 배

import sys

input = sys.stdin.readline

n = int(input().rstrip())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input().rstrip())
boxes = sorted(list(map(int, input().split())), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

answer = 0
position = [0 for _ in range(n)] # 각 크레인이 현재 옮겨야 하는 박스의 번호
completion = [False for _ in range(len(boxes))]

count = 0
while True:
    if count == len(boxes):
        break
    for i in range(n):
        while position[i] < len(boxes):
            if not completion[position[i]] and boxes[position[i]] <= cranes[i]:
                completion[position[i]] = True
                position[i] += 1
                count += 1 # 실은 박스의 개수
                break
            position[i] += 1
    answer += 1
print(answer)

# while False in completion:
#     idx = [idx for idx, val in enumerate(completion) if val == False][0]
#     for crane in cranes:
#         while idx < len(boxes):
#             if completion[idx] == False and boxes[idx] <= crane: # 아직 옮겨지지 않았고, 크레인에 실을 수 있으면
#                 completion[idx] = True
#                 idx += 1
#                 break
#             else: # 크레인에 실을 수 없으면 다음 크레인 보기
#                 idx += 1
#     answer += 1

# print(answer)