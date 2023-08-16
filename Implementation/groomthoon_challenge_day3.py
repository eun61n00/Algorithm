# -*- coding: utf-8 -*-
# 구름톤 챌린지 3일차
# 합 계산기

n = int(input())
answer = 0
for _ in range(n):
    n1, operator, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    if operator == '+':
        tmp = n1 + n2
    elif operator == '-':
        tmp = n1 - n2
    elif operator == '*':
        tmp = n1 * n2
    else:
        tmp = n1 // n2
    answer += tmp
print(answer)