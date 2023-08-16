# -*- coding: utf-8 -*-
# 구름톤 챌린지 2일차
# 프러덕트 매니징

N = int(input())
T, M = map(int, input().split())
tasks = [int(input()) for _ in range(N)]

total = sum(tasks)
t_add, m_add = total // 60, total % 60

T += t_add
M += m_add

if M > 59:
    T += (M // 60)
    M %= 60

    if T > 23:
    T %= 24

    print(T, M)