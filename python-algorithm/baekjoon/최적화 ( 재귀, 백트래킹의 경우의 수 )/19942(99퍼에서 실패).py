# 다이어트
import sys

INF = sys.maxsize


def recusrive(idx, p, f, s, v, c, idx_list):
    global answer
    global answer_idx

    if idx == n:
        if min_ingredients[0] <= p and min_ingredients[1] <= f and min_ingredients[2] <= s and min_ingredients[3] <= v:
            if answer > c:
                answer = c
                answer_idx = idx_list[:]
        return

    idx_list.append(idx + 1)
    recusrive(idx + 1,
              p + ingredients[idx][0],
              f + ingredients[idx][1],
              s + ingredients[idx][2],
              v + ingredients[idx][3],
              c + ingredients[idx][4],
              idx_list
              )
    idx_list.pop()
    recusrive(idx + 1, p, f, s, v, c, idx_list)


n = int(input())
min_ingredients = list(map(int, input().split()))
ingredients = []
answer = INF
answer_idx = []

for _ in range(n):
    ingredient = list(map(int, input().split()))
    ingredients.append(ingredient)

idx_list = []
recusrive(0, 0, 0, 0, 0, 0, idx_list)

if answer == INF:
    print(-1)
else:
    print(answer)
    print(*answer_idx)
