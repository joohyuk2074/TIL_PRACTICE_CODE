# Default input 스트링 타입, 문자열 타입으로 받아와주도록 만들어짐!

# Case 1 : 단순히 정수 일 때,
number = int(input())

# Case 2 : 여러가지 숫자들의 조합, 수열
list1 = list(map(int, input().split()))

# Case 3: 단순히 문자 일 때,
string = input()

# Case 4: 여러가지 문자들의 조합, 문자열
list2 = list(map(str, input().split()))

# 반복문
for _ in range(100):
    print("hi")

number = 0
while number < 10:
    print(number)
    number += 1
