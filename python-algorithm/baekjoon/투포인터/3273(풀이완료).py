n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

idx1 = 0
idx2 = n - 1

answer = 0
while idx1 < idx2:
    if arr[idx1] + arr[idx2] == x:
        answer += 1
        idx1 += 1
        idx2 -= 1
    elif arr[idx1] + arr[idx2] < x:
        idx1 += 1
    else:
        idx2 -= 1

print(answer)
