# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 6198 옥상 정원 꾸미기

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(int(input()))

stack = []
answer = [0] * n
count = 0

# 내가 이전 빌딩에서 보여질 수 있는지 확인
for idx, height in enumerate(buildings):
    while stack:
        if stack[-1][1] == height:  # 이전 빌딩에서 보여질 수 없지만 그 뒤에는 볼 수 없으므로 pop
            # count += (idx - stack[-1][0])
            stack.pop()
        if stack[-1][1] < height:  # 나 이전까지 보여짐
            count += (idx - stack[-1][0] - 1)
            print(stack, count)
            stack.pop()
        else:
            break
    stack.append((idx, height))
    # print(idx, height, stack)

# print(count, stack)

while len(stack) > 1:
    idx, height = stack.pop()
    if stack[-1][1] > height:  # 볼 수 있음
        count += (idx - stack[-1][0])

print(stack)
print(count)
