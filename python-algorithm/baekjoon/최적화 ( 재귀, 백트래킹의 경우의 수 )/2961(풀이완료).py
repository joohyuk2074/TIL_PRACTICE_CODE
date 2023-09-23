# 도영이가 만든 맛있는 음식
def recursive(idx, s_multiple, b_sum, n, ingredients):
    if idx >= n:
        if s_multiple == 1 and b_sum == 0:
            return 2_000_000_000
        else:
            return abs(s_multiple - b_sum)

    result1 = recursive(idx + 1, s_multiple * ingredients[idx][0], b_sum + ingredients[idx][1], n, ingredients)
    result2 = recursive(idx + 1, s_multiple, b_sum, n, ingredients)
    return min(result1, result2)


n = int(input())
ingredients = []
for _ in range(n):
    s, b = map(int, input().split())
    ingredients.append([s, b])

supports_dunder_lt_supports_dunder_gt = recursive(0, 1, 0, n, ingredients)
print(supports_dunder_lt_supports_dunder_gt)
