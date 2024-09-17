def solution(bandage, health, attacks):

    bandage_time, x, y = bandage
    max_health = health

    series = 0
    for i in range(1, attacks[-1][0] + 1):  # 마지막 공격 시간까지 돌기
        if attacks[0][0] == i:  # 공격
            time, amount = attacks.pop(0)
            health -= amount
            if health <= 0:
                return -1
            series = 0  # 연속 성공 초기화
        else:
            series += 1  # 연속 성공
            health += x
            health = min(max_health, health)
            if health > max_health:
                health = max_health
            if series == bandage_time:
                health += y
                health = min(max_health, health)
                series = 0
    return health
