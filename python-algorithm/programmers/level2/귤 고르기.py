def solution(k, tangerine):
    answer = 0

    t_map = dict()  # O(n)
    for n in tangerine:
        if n in t_map:
            t_map[n] += 1
        else:
            t_map[n] = 1

    sorted_dict = dict(sorted(t_map.items(), key=lambda item: item[1], reverse=True))  # O(nlogn)

    for key in sorted_dict:  # O(n)
        value = sorted_dict[key]

        if k <= value:
            answer += 1
            break
        else:
            k -= value
            answer += 1

    return answer


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
