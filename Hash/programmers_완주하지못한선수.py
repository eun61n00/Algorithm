# -*- coding: utf-8 -*-
# 프로그래머스 완주하지 못한 선수

def solution(participant, completion):
	for complete in completion:
		if complete in participant:
			participant.remove(complete)

	return participant[0]

def solution(participant, completion):

	participant.sort()
	completion.sort()

	for i in range(len(completion)):
		if completion[i] != participant[i]:
			return participant[i]
	return participant[-1]