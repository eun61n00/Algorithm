# !/usr/bin/python3
# -*- coding: utf-8 -*-
# programmers 옹알이

def solution(babblings):
    answer = 0

    for babbling in babblings:
        while babbling:
            if babbling[:3] == "aya" or babbling[:3] == "woo":
                if len(babbling) == 3:
                    answer += 1
                    break
                else:
                    babbling = babbling[3:]
            elif babbling[:2] == "ye" or babbling[:2] == "ma":
                if len(babbling) == 2:
                    answer += 1
                    break
                else:
                    babbling = babbling[2:]
            else:
                break
    return answer