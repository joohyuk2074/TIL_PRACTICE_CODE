from functools import reduce
# lambda 매개변수 : 표현식

def hap(x, y):
    return x + y


(lambda x, y: x + y)(10, 20)


# map(함수, 리스트)
m = list(map(lambda x: x ** 2, range(5)))
print(m)

i = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
print(i)
