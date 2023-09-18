# 숫자야구

def get_strike_cnt(number1, number2):
    strike_cnt = 0
    for i in range(len(number1)):
        if int(number1[i]) == int(number2[i]):
            strike_cnt += 1
    return strike_cnt


def get_ball_cnt(number1, number2):
    ball_cnt = 0
    for i in range(len(number1)):
        for j in range(len(number2)):
            if i != j and int(number1[i]) == int(number2[j]):
                ball_cnt += 1
    return ball_cnt


def recur(hint_idx, number):
    global answer

    if hint_idx == n:
        answer += 1
        recur(0, number + 1)
        return

    if number == 1000:
        return
        # 만약에 hint에 통과했다면
    hints = hint[hint_idx]
    hint_number = hints[0]
    strike_cnt = hints[1]
    ball_cnt = hints[2]

    calculated_strike_cnt = get_strike_cnt(str(number), str(hint_number))
    calculated_ball_cnt = get_ball_cnt(str(number), str(hint_number))

    if strike_cnt == calculated_strike_cnt and ball_cnt == calculated_ball_cnt:
        recur(hint_idx + 1, number)

    recur(0, number + 1)


n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0
recur(0, 100)
print(answer)
