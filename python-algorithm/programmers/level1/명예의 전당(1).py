def solution(k, score):
    answer = []

    hall_of_fame = []
    for num in score:
        if len(hall_of_fame) < k:
            hall_of_fame.append(num)
        else:
            hall_of_fame.sort()
            for i in range(0, len(hall_of_fame)):
                if hall_of_fame[i] < num:
                    hall_of_fame[i] = num
                    break

        min_score = min(hall_of_fame)
        answer.append(min_score)

    return answer


def other_solution(k, score):
    q = []
    answer = []

    for s in score:
        q.append(s)
        if len(q) > k:
            q.remove(min(q))
        answer.append(min(q))


k = 3
score = [10, 100, 20, 150, 1, 100, 200]

print(solution(k, score))
