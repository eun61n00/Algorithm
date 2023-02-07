# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    job_cnt = len(jobs)

    for job in jobs:
        tmp = job[1]
        job[1] = job[0]
        job[0] = tmp

    heapq.heapify(jobs)

    while jobs:
        popped_job = heapq.heappop(jobs)
        answer += answer + popped_job[0] - popped_job[1]

    return answer // job_cnt

print(solution([[0, 3], [1, 9], [2, 6]]))