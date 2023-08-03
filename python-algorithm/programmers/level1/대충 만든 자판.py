def solution(keymap, targets):
    answer = []

    for target in targets:
        cnt = 0

        for c in target:
            min_index = get_min_index(c, keymap)
            # 최소 min_idx를 구함
            if min_index == -1:
                cnt += (-1_000_000_000)
            else:
                cnt += (min_index + 1)

        if cnt < 0:
            answer.append(-1)
        else:
            answer.append(cnt)

    return answer


def get_min_index(c, keymap):
    min_idx = 1_000_000_000
    for key in keymap:
        index = key.find(c)
        if index == -1:
            continue
        if min_idx > index:
            min_idx = index

    if min_idx == 1_000_000_000:
        return -1

    return min_idx


keymap1 = ["ABACD", "BCEFD"]
targets1 = ["ABCD", "AABB"]
print(solution(keymap1, targets1))
keymap2 = ["AA"]
targets2 = ["B"]
print(solution(keymap2, targets2))
keymap3 = ["BC"]
targets3 = ["AC", "BC"]
print(solution(keymap3, targets3))
