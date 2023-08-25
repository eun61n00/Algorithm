# usr/bin/env python
# -*- coding: utf8 -*-
# programmers PCCP 모의고사 1회 2번) 체육 대회

from itertools import permutations

def solution(ability):
    answer = []
    subjects = list(map(list, zip(*ability)))
    permutation = permutations(range(len(ability)), len(ability[0]))
    for p in list(permutation):
        tmp = 0
        for i, subject in enumerate(subjects):
            tmp += subject[p[i]]
        answer.append(tmp)
    return max(answer)