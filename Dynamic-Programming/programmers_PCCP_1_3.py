# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 프로그래머스 PCCP 모의고사 1회 3번 유전법칙

# 시간초과
def solution(queries):
    answer = []
    dictionary = {}
    dictionary['RR'] = ['RR', 'RR', 'RR', 'RR']
    dictionary['Rr'] = ['RR', 'Rr', 'Rr', 'rr']
    dictionary['rr'] = ['rr', 'rr', 'rr', 'rr']
    for query in queries:
        n, p = query[0], query[1]
        generations = [[] for _ in range(n + 1)] # 세대별 개체 저장
        generations[1].append('Rr') # 1세대
        for i in range(2, n + 1):
            for j in generations[i - 1]:
                generations[i] += dictionary[j]
        answer.append(generations[n][p - 1])
    return answer

solution(input())