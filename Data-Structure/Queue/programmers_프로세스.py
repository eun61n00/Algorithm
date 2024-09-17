# -*- coding: utf-8 -*-
# 프로그래머스 프로세스

from collections import deque


def solution(priorities, location):
    cnt = 0

    complete = []
    priorities = deque(priorities)

    while location != -1:

        if priorities[0] == max(priorities):
            complete.append(priorities.popleft())
            location -= 1
        else:
            priorities.append(priorities.popleft())
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return len(complete)
