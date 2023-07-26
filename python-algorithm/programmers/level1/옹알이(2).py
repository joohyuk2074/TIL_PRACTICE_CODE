def solution(babbling):
    answer = 0

    words = ["aya", "ye", "woo", "ma"]

    for t in babbling:
        text = ""
        prev_index = -1
        complete_text = ""

        for i in range(len(t)):
            text += t[i]
            for j in range(len(words)):
                if text == words[j] and prev_index != j:
                    prev_index = j
                    complete_text += text
                    text = ""
                    break
        if t == complete_text:
            answer += 1

    return answer


def other_solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            if j * 2 not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            answer += 1
    return answer


input1 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
input2 = ["aya", "yee", "u", "maa"]
print(solution(input2))
