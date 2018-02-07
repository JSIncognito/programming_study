# 2.7.7 함수형 도구


def exp(base, power):
    return base ** power

# def two_to_the(power):
#     return exp(2, power)

from functools import partial
two_to_the = partial(exp, 2)
print(two_to_the(3))

square_of = partial(exp, power=2)
print(square_of(3))

# list comprehension 의 대안으로, map, reduce, filter 를 사용하는 경우도 있다.
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
print(twice_xs)
twice_xs = list(map(double, xs))
print(twice_xs)

list_double = partial(map, double)
twice_xs = list(list_double(xs))
print(twice_xs)

# 여러 개의 list 를 입력해 주면 인자가 여러 개인 함수에도 map 를 적용할 수 있다.
def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5])

# filter 는 if 가 포함된 list comprehension 과 동일하다.
def is_even(x):
    """x 가 짝수면 True, 홀수면 false"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print(x_evens)

x_evens = filter(is_even, xs)
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)
print(type(x_evens))
print(list(x_evens))

# 그리고 reduce 는 list 의 모든 항목을 순차적으로 합쳐 주면서 list 를 하나의 값으로 표현한다.
from functools import reduce
x_product = reduce(multiply, xs)
print(x_product)
list_product = partial(reduce, multiply)
x_product = list_product(xs)
print(x_product)

