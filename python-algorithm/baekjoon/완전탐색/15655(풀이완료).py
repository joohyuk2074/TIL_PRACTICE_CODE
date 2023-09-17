def recurisve(index, result, number, n, m, numbers):
    if number == m:
        print(result)
        return

    for i in range(index, n):
        recurisve(i + 1, result + str(numbers[i]) + ' ', number + 1, n, m, numbers)


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
flags = [False for _ in range(n)]
recurisve(0, '', 0, n, m, numbers)
