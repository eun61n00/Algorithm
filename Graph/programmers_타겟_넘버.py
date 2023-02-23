# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 타겟 넘버


# BFS
def solution(numbers, target):
    results = [0]
    for num in numbers:
        tmp = []
        for result in results:
            tmp.append(result + num)
            tmp.append(result - num)
        results = tmp
    return results.count(target)


# DFS
answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                global answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    dfs(0,0)
    return answer