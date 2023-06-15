# !/usr/bin/python3
# -*- coding: utf-8 -*-
# programmers 옹알이2

def solution(babblings):
    answer = 0

    for babbling in babblings:
        prev = ""
        while babbling:
            if babbling[:3] == "aya" and prev != "aya":
                if len(babbling) == 3:
                    answer += 1
                    break
                babbling = babbling[3:]
                prev = "aya"
            elif babbling[:3] == "woo" and prev != "woo":
                if len(babbling) == 3:
                    answer += 1
                    break
                babbling = babbling[3:]
                prev = "woo"
            elif babbling[:2] == "ye" and prev != "ye":
                if len(babbling) == 2:
                    answer += 1
                    break
                babbling = babbling[2:]
                prev = "ye"
            elif babbling[:2] == "ma" and prev != "ma":
                if len(babbling) == 2:
                    answer += 1
                    break
                babbling = babbling[2:]
                prev = "ma"
            else:
                break
    return answer