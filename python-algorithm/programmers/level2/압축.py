def solution(msg):
    answer = []

    alpha = [''] * 1001
    for i in range(ord('A'), ord('Z') + 1):
        alpha[i - 64] = chr(i)
    count = 26

    idx = 0
    while idx < len(msg):
        index = idx
        word = msg[index]
        while getIndexIfPresent(word, alpha) != 0:
            index += 1
            if index < len(msg):
                word += msg[index]
            else:
                break
        if index < len(msg):
            count += 1
            alpha[count] = word
            answer.append(getIndexIfPresent(word[:-1], alpha))
            idx += len(word[:-1])
        else:
            answer.append(getIndexIfPresent(word, alpha))
            break;
    return answer


def getIndexIfPresent(c, alpha):
    for i in range(1, len(alpha)):
        if alpha[i] == c:
            return i
    return 0


msg = "KAKAO"
print(solution(msg))
