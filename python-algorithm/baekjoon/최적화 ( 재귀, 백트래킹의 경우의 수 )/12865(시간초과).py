def recursive(index, weight, value):
    global answer

    if weight > k:
        return

    if index == n:
        if answer < value:
            answer = value
        return

    recursive(index + 1, weight + inputs[index][0], value + inputs[index][1])
    recursive(index + 1, weight, value)


n, k = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recursive(0, 0, 0)

print(answer)
