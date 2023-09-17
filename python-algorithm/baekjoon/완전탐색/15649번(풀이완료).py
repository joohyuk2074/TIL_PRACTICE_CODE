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
numbers = [i for i in range(1, n + 1)]
flags = [False for _ in range(n)]
recurisve('', 0, n, m, numbers, flags)

# # 반복문
#
# for i in range(n):
#     flags[i] = True
#     for j in range(n):
#         if not flags[j] and i != j:
#             print(numbers[i], numbers[j])
#             flags[i] = False
