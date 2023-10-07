n = int(input())
arr1 = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))

result = []
for number in arr2:
    s = 0
    e = n - 1
    flag = False

    while s <= e:
        mid = (s + e) // 2

        if number == arr1[mid]:
            flag = True
            break

        if number < arr1[mid]:
            e = mid - 1
        else:
            s = mid + 1

    if flag:
        result.append(1)
    else:
        result.append(0)
    flag = False

print(' '.join(map(str, result)))
