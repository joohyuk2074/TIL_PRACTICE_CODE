def solution_timeout(topping):
    answer = 0

    for i in range(len(topping)):
        # i = 배열의 경계
        front_topping = set(topping[0:i])
        end_topping = set(topping[i:len(topping) + 1])
        if len(front_topping) == len(end_topping):
            answer += 1

    return answer


def solution(topping):
    answer = 0

    topping_set = set()
    topping_dict = {}
    for t in topping:
        if t in topping_dict:
            topping_dict[t] += 1
        else:
            topping_dict[t] = 1

    for i in range(len(topping)):
        t = topping[i]
        topping_dict[t] -= 1
        if topping_dict[t] == 0:
            del topping_dict[t]
        topping_set.add(t)

        if len(topping_set) == len(topping_dict):
            answer += 1

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))
