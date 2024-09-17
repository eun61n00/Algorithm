# -*- coding: utf-8 -*-
# 프로그래머스 모의고사

def solution(answers):
	result = []

	supoja1 = [1, 2, 3, 4, 5]
	supoja1_answer = [supoja1[i%len(supoja1)] for i in range(len(answers))]
	supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
	supoja2_answer = [supoja2[i%len(supoja2)] for i in range(len(answers))]
	supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	supoja3_answer = [supoja3[i%len(supoja3)] for i in range(len(answers))]

	cnt1 = [True if answers[i] == supoja1_answer[i] else False for i in range(len(answers))]
	cnt1 = cnt1.count(True)
	cnt2 = [True if answers[i] == supoja2_answer[i] else False for i in range(len(answers))]
	cnt2 = cnt2.count(True)
	cnt3 = [True if answers[i] == supoja3_answer[i] else False for i in range(len(answers))]
	cnt3 = cnt3.count(True)
	cnt_list = [cnt1, cnt2, cnt3]

	for i in range(3):
		if cnt_list[i] == max(cnt_list):
			result.append(i + 1)

	return result

print(solution([1,2,3,4,5]	))