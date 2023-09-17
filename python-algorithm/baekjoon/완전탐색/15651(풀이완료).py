def recurisve(result, number, n, m, numbers):
    if number == m:
        print(result)
        return

    for i in range(n):
        recurisve(result + str(numbers[i]) + ' ', number + 1, n, m, numbers)


n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
flags = [False for _ in range(n)]
recurisve('', 0, n, m, numbers)
