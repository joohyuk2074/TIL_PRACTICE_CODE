def recursive(index, current_a, current_b):
    global answer

    if index == n:
        if current_a == 1 and current_b == 0:
            return

        if answer > abs(current_a - current_b):
            answer = abs(current_a - current_b)

        return

    recursive(index + 1, current_a * inputs[index][0], current_b + inputs[index][1])
    recursive(index + 1, current_a, current_b)


n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]
answer = 10 ** 9

recursive(0, 1, 0)

print(answer)
