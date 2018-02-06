# 4.7 함수
# 매개변수가 없지만 True 값을 반환하는 함수를 정의
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

# 매개변수 함수
def echo(anything):
    return anything + ' ' + anything

print(echo("Rumplestiltskin"))

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've naver heard of the color " + color + "."

comment=commentary('blue')
print("commentary(blue) : ",comment)

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

print("is_none : ",is_none(None))
print("is_none : ",is_none(True))
print("is_none : ",is_none(False))
print("is_none : ",is_none(0))

# 4.7.1 위치 인자
# 파이썬은 다른 언어에 비해 함수의 인자를 유연하고 독특하게 처리한다.
# 인자의 가장 익숙한 타입은 값을 순서대로 상응하는 매개변수에 복사하는 위치 인자 positional arguments 다 .
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken', 'cake'))
# 매우 일반적이지만 위치 인자의 단점은 각 위치의 의미를 알아야 한다는 것이다. 다음 예제에서 첫 번째 인자 대신 마지막 인자를
# wine 으로 menu() 를 호출하면 매우 이상하게 된다.
print(menu('beef', 'bagel', 'bordeaux'))

# 4.7.2 키워드 인자
# 위치 인자의 혼동을 피하기 위해 매개변수에 상응하는 이름을 인자에 지정할 수 있다.
# 심지어 인자를 함수의 정의와 다른 순서로 지정할 수 있다.
print(menu(entree="beef", dessert="bagel", wine="bordeaux"))

# 위치 인자와 키워드 인자를 섞어서 쓸 수 있다.
print(menu('frontenac', dessert='flan', entree='fish'))
# 위치 인자와 키워드 인자로 함수를 호출한다면 위치 인자가 먼저 와야 한다.

# 4.7.3 기본 매개변수값 지정하기
def munu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

#print(menu(wine = 'chardonnay', entree='chicken'))
# dessert 인자를 입력하면 기본값 대신 입력한 인자가 사용된다.
print(menu('dunkelfelder', 'duck', 'doughnut'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def works(arg):
    result = []
    result.append(arg)
    return result

print("works a :",works('a'))
print("works b :",works('b'))

# 첫 번 째 인자 호출을 가리키기 위해 매개변수에 다른 값을 넣어서 수정할 수 있다.
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print("non : ",result)

nonbuggy('a')
nonbuggy('b')

# 4.7.4 위치 인자 모으기: *
# 애스터리스트(*) 를 어떤 것을 가리키는 포인터가 아니다. 함수의 매개변수에 애스터리스크를 사용할때,
# 애스터리스크는 매개변수에서 위치 인자 변수들을 튜플로 묶는다.

def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest: ', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

#* 를 사용할 때 가변 인자의 이름으로 args 를 사용할 필요가 없지만 관용적으로 args 를 사용한다.

# 4.7.5 키워드 인자 모으기: **
def print_kwargs(**kwargs):
    print('Keyowrd arguments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# args 와 마찬가지로 키워드 매개변수의 이름을 kwargs 로 할 필요는 없지만 관용적으로 kwargs 를 사용한다.

# 4.7.6 docstring
def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. It it i, print the *first* argument.

    :param thing:
    :param check:
    :return:
    '''
    if check:
        print(thing)
help(echo)
print(echo.__doc__)
# __doc__ 은 docstring 의 내부 이름인 함수 내의 변수다.


