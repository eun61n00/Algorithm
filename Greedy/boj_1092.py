# usr/bin/env python
# -*- coding: utf8 -*-
# boj 1092 배

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

answer = 0

while boxes:
    idx = 0
    # 놀고 있는 크레인이 없도록
    for crane in cranes:
        # 모든 박스를 검사하면서 크레인에 실을 수 있는지 검사
        while idx < len(boxes):
            if boxes[idx] <= crane:
                boxes.pop(idx)
                break
            else:
                idx += 1
    answer += 1

print(answer)

completion = [False for _ in range(len(boxes))]

while False in completion:
    idx = 0
    for crane in cranes:
        while idx < len(boxes):
            if completion[idx] == False and boxes[idx] <= crane:
                completion[idx] = True
                break
            else:
                idx += 1
    answer += 1

print(answer)