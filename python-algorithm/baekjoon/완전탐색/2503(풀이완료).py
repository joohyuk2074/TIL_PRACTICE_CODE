n = int(input())
infos = []
for _ in range(n):
    number, s, b = map(int, input().split())
    infos.append([number, s, b])

answer = 0
for num in range(123, 999):
    num_str = str(num)
    if '0' in num_str:
        continue

    if num_str[0] != num_str[1] and num_str[1] != num_str[2] and num_str[0] != num_str[2]:
        flag = True
        for number, s, b in infos:
            s_cnt, b_cnt = 0, 0

            num_str2 = str(number)

            for i in range(0, 3):
                for j in range(0, 3):
                    if num_str[i] == num_str2[j]:
                        if i == j:
                            s_cnt += 1
                        else:
                            b_cnt += 1

            if s != s_cnt or b != b_cnt:
                flag = False

        if flag:
            answer += 1

print(answer)
