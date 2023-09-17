n, h = map(int, input().split())
height = []
for _ in range(n):
    height.append(int(input()))

new_map = [[0 for _ in range(h + 1)] for _ in range(n)]
for i in range(n):
    if i == 0 or i % 2 == 0:  # 석순인 경우
        new_map[i][0] = 1
        new_map[i][height[i]] = -1
    else:  # 종유석 인 경우
        new_map[i][h] = -1
        new_map[i][h - height[i]] = 1

results = []
for column in range(h):
    sum = 0
    for row in range(n):
        sum += new_map[row][column]
    results.append(sum)

# 누적합 구하기
answers = [0] * h
answers[0] = results[0]
for i in range(1, h):
    answers[i] = answers[i-1] + results[i]

sorted_arr = sorted(answers)
min_num = min(sorted_arr)

answer = 0
for i in range(h):
    if sorted_arr[i] == min_num:
        answer += 1

print(min_num, answer)
