# n, m = map(int, input().split())
#
# table = []
# for _ in range(n):
#     table.append(list(map(int, input().split())))
#
import sys

n, m = map(int, sys.stdin.readline().split())

table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))


# 누적합 구하기
cumulative_sum_map = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        cumulative_sum_map[i + 1][j + 1] = cumulative_sum_map[i][j + 1] + cumulative_sum_map[i + 1][j] - \
                                           cumulative_sum_map[i][j] + table[i][j]

for _ in range(m):
    input_list = list(map(int, input().split()))
    x1 = input_list[0]
    y1 = input_list[1]
    x2 = input_list[2]
    y2 = input_list[3]

    answer = cumulative_sum_map[x2][y2] - cumulative_sum_map[x1 - 1][y2] - cumulative_sum_map[x2][y1 - 1] + cumulative_sum_map[x1 - 1][y1 - 1]

    print(answer)
