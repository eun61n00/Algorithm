# -*- coding: utf-8 -*-
# 프로그래머스 의상

def solution(clothes):
    clothes_dict = {}

    for cloth in clothes:
        if cloth[1] not in list(clothes_dict.keys()):
            clothes_dict[cloth[1]] = [cloth[0]]
        clothes_dict[cloth[1]].append(cloth[0])

    answer = 1
    for cloth_key in clothes_dict.keys():
        answer *= len(clothes_dict[cloth_key])

    return answer - 1


def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


solution2([["yellow_hat", "headgear"], ["blue_sunglasses",
          "eyewear"], ["green_turban", "headgear"]])
