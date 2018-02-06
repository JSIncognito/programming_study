# '모든 것이 객체다'. 객체는 숫자, 문자열, 튜플, 리스트, 딕셔너리, 그리고 함수를 포함한다.
# 파이썬에서 함수는 일등 시민 이다. 이 뜻은 함수를 변수에 할당할 수 있고, 다른 함수에서 이를 인자로 쓸 수 있으며,
# 함수에서 이를 반환할 수 있다는 것이다.
def answer():
    print(42)

def run_something(func):
    func()

run_something(answer)
# answer() 를 전달하는 것이 아니라 answer 를 전달했다. 파이썬에서 괄호 () 는 함수를 호출한다는 의미다.
# 괄호가 없으면 함수를 다른 모든 객체와 마찬가지로 간주한다. 파이썬에서 모든 것은 객체기 때문이다.

def add_args(arg1, arg2):
    print(arg1 + arg2)
print(type(add_args))

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 5, 9)
# *args, **kwargs 인자와 결합해서 사용할 수 있다.
# sum() 함수를 사용해서 이 인자들을 더한 값을 반환한다.
def sum_args(*args):
    return sum(args)
# sum() 함수는 순회 가능한 숫자 (정수 혹은 부동소수점수) 인자의 값을 모두 더하는 파이썬 내장 함수다.
def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))
# 함수를 리스트, 튜플, 셋, 딕셔너리의 요소로 사용할 수 있다. 함수는 불변하기 때문에 딕셔너리의 키로도 사용할 수 있다.
