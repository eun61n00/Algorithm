from collections import defaultdict


def solution(enroll, referral, seller, amount):

    members_dict = defaultdict(int)
    members_dict["center"] = 0
    for idx, member in enumerate(enroll):
        members_dict[member] = idx + 1

    members = [[] for _ in range(len(enroll) + 1)]
    for i, r in enumerate(referral):
        if r == "-":
            members[i + 1].append(0)
        else:
            members[i + 1].append(members_dict[r])
    global result
    result = [0] * (len(enroll) + 1)

    for s, a in zip(seller, amount):
        dfs(members_dict[s], a*100, members)

    return result[1:]


def dfs(v, a, graph):
    if int(a) == 0:
        return
    result[v] += int(a)
    for i in graph[v]:
        result[v] -= int(a * 0.1)
        dfs(i, a * 0.1, graph)
