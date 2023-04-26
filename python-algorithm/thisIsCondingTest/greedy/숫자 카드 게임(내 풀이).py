n, m = map(int, input().split())

arr = []
answer = 0
for _ in range(n):
    row = list(map(int, input().split()))
    row.sort()
    if answer < row[0]:
        answer = row[0]

print(answer)