# -*- coding: utf-8 -*-
# 프로그래머스 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
	time = 0
	completion_cnt = 0
	completion = len(truck_weights)
	on_bridge = deque([0 for _ in range(bridge_length)])
	truck_weights = deque(truck_weights)
	on_bridge_sum = 0

	while completion_cnt < completion:
		time += 1
		arrived = on_bridge.popleft()
		if arrived != 0:
			on_bridge_sum -= arrived
			completion_cnt += 1

		if len(truck_weights) != 0 and on_bridge_sum + truck_weights[0] <= weight: # 트럭 하나더
			on_bridge.append(truck_weights.popleft())
			on_bridge_sum += on_bridge[-1]
		else:
			on_bridge.append(0)

	return time

DUMMY_TRUCK = 0

class Bridge(object):

	def __init__(self, length, weight):
		self._max_length = length
		self._max_weight = weight
		self._queue = deque()
		self._current_weight = 0

	def push(self, truck):
		next_weight = self._current_weight + truck
		if next_weight <= self._max_weight and len(self._queue) < self._max_length:
			self._queue.append(truck)
			self._current_weight = next_weight
			return True
		else:
			return False

	def pop(self):
		item = self._queue.popleft()
		self._current_weight -= item
		return item

	def __len__(self):
		return len(self._queue)

	def __repr__(self):
		return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution2(bridge_length, weight, truck_weights):
	bridge = Bridge(bridge_length, weight)
	trucks = deque(w for w in truck_weights)

	for _ in range(bridge_length):
		bridge.push(DUMMY_TRUCK)

	count = 0
	while trucks:
		bridge.pop()

		if bridge.push(trucks[0]):
			trucks.popleft()
		else:
			bridge.push(DUMMY_TRUCK)

		count += 1

	while bridge:
		bridge.pop()
		count += 1

	return count