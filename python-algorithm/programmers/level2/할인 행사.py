import copy


def solution(want, number, discount):
    answer = 0

    want_to_num_map = dict(zip(want, number))

    end = len(discount) - 10 + 1
    for i in range(0, end):
        map = copy.deepcopy(want_to_num_map)
        flag = True

        arr = discount[i: i + 10]
        for s in arr:
            if s in map:
                map[s] -= 1

        for value in map.values():
            if value > 0:
                flag = False
                break

        if flag:
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
            "apple", "banana"]
print(solution(want, number, discount))
