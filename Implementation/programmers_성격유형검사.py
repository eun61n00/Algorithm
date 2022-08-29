# -*- coding: utf-8 -*-
# 프로그래머스 성격유형검사

def solution(survey, choices):
    answer = ""
    personalities = "RTCFJMAN"

    score_dict = {}
    for i in range(len(personalities)):
        score_dict[personalities[i]] = 0

    for i in range(len(survey)):
        ele1 = survey[i][0]
        ele2 = survey[i][1]

        if choices[i] <= 4:
            score_dict[ele1] += 4 - choices[i]
        else:
            score_dict[ele2] += choices[i] - 4

    if score_dict["R"] >= score_dict["T"]:
        answer += "R"
    else:
        answer += "T"

    if score_dict["C"] >= score_dict["F"]:
        answer += "C"
    else:
        answer += "F"

    if score_dict["J"] >= score_dict["M"]:
        answer += "J"
    else:
        answer += "M"

    if score_dict["A"] >= score_dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer