def recurisve(index, result, number, n, m, numbers):
    if number == m:
        print(result)
        return

    for i in range(index, n):
        recurisve(i, result + str(numbers[i]) + ' ', number + 1, n, m, numbers)


n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
recurisve(0, '', 0, n, m, numbers)
