# -*- coding: utf-8 -*-
# 프로그래머스 H-index

def solution(citations):
    h_idx = 0

    citations.sort(reverse = True)

    for i, citation in enumerate(citations):
        temp = min(i + 1, citation)
        if temp > h_idx:
            h_idx = temp
        else:
            return h_idx
    return h_idx