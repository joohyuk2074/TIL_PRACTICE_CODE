def solution(cards):
    answer = 0

    check = [False] * (len(cards) + 1)

    number_to_idx = {}
    for i in range(0, len(cards)):
        key = i + 1
        value = cards[i]
        number_to_idx[key] = value

    result = []
    for i in range(1, len(cards) + 1):
        idx = i

        part = set()
        while check[idx] is False:
            check[idx] = True
            part.add(idx)
            idx = number_to_idx[idx]
        if part:
            result.append(len(part))

    results = sorted(result, reverse=True)

    if len(results) == 1:
        return 0

    answer = results[0] * results[1]

    return answer


cards = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution(cards))
