from collections import defaultdict


def solution(weights):
    answer = 0

    # 시소 거리에 따른 무게 배열
    weights_distance = [0] * 4001
    # 실제 무게 배열
    weight_arr = [0] * 1001

    for weight in weights:
        # 시소의 거리에 따른 무게
        score1 = weight * 2
        score2 = weight * 3
        score3 = weight * 4

        # 이전에 지나간 사람이 현재 해당 무게와 일치하는 값이 있으면 각각의 사람들과 시소짝궁으로 추가함
        answer += weights_distance[score1]
        answer += weights_distance[score2]
        answer += weights_distance[score3]

        if weight_arr[weight] > 0:
            answer -= weight_arr[weight] * 2

        weight_arr[weight] += 1
        weights_distance[score1] += 1
        weights_distance[score2] += 1
        weights_distance[score3] += 1

    return answer


def other_solution(weights):
    answer = 0
    info = defaultdict(int)

    for w in weights:
        answer += info[w]

    print(info)
    return answer


# weights = [100, 180, 360, 100, 270]
# print(solution(weights))
weights = [100, 180, 360, 100, 270]
print(other_solution(weights))
