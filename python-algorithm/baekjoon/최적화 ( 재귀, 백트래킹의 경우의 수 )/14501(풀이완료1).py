def recursive(index, price):
    global answer

    if index > n:
        return

    if index == n:
        if answer < price:
            answer = price
        return

    recursive(index + inputs[index][0], price + inputs[index][1])
    recursive(index + 1, price)


n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recursive(0, 0)

print(answer)
