# usr/bin/env python
# -*- coding: utf8 -*-
# programmers PCCP 모의고사 1회 1번) 외톨이 알파벳

from collections import defaultdict

def solution(input_string):
    answer = ''
    char_dict = defaultdict(list)
    for i, ch in enumerate(input_string):
        char_dict[ch].append(i)
    for ch in char_dict:
        if len(char_dict[ch]) == 1:
            continue
        for idx in range(0, len(char_dict[ch]) - 1):
            if char_dict[ch][idx + 1] - char_dict[ch][idx] > 1:
                answer += ch
                break
    answer = sorted(list(answer))
    if len(answer) == 0:
        return "N"
    else:
        return ''.join(answer)
