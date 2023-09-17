def recurisve(result, number, n, m, numbers, flags):
    if number == m:
        print(result)
        return

    for i in range(n):
        if not flags[i]:
            flags[i] = True
            recurisve(result + str(numbers[i]) + ' ', number + 1, n, m, numbers, flags)
            flags[i] = False


n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
flags = [False for _ in range(n)]
recurisve('', 0, n, m, numbers, flags)
