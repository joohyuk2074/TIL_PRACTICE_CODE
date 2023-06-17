def solution(k, m, score):
    answer = 0

    score_length = len(score)
    box_cnt = score_length // m

    if box_cnt <= 0:
        return 0

    sorted_score = sorted(score, reverse=True)

    box = []
    # cnt = 0
    for s in sorted_score:
        if len(box) == m:
            answer += min(box) * m
            box = [s]
            # cnt += 1
        else:
            box.append(s)

    if len(box) == m:
        answer += min(box) * m

    return answer


def other_solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m]) * m


k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
