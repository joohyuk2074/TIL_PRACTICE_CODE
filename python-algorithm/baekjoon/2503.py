# 숫자 야구

n = int(input())
condition_list = [list(map(int, input().split())) for _ in range(4)]

answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:

                number1 = str(i) + str(j) + str(k)

                cnt = 0
                for condition in condition_list:
                    number2 = str(condition[0])
                    strike = condition[1]
                    ball = condition[2]

                    ball_count = 0
                    strike_count = 0

                    for idx1 in range(0, 3):
                        for idx2 in range(0, 3):
                            if number1[idx1] == number2[idx2]:
                                if idx1 != idx2:
                                    ball_count += 1
                                else:
                                    strike_count += 1

                    if ball == ball_count and strike == strike_count:
                        cnt += 1

                if cnt == n:
                    answer += 1

print(answer)
