def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = -1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer


keymap1 = ["ABACD", "BCEFD"]
targets1 = ["ABCD", "AABB"]
print(solution(keymap1, targets1))
# keymap2 = ["AA"]
# targets2 = ["B"]
# print(solution(keymap2, targets2))
# keymap3 = ["BC"]
# targets3 = ["AC", "BC"]
# print(solution(keymap3, targets3))
