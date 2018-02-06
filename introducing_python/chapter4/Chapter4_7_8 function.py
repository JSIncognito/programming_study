# 4.7.8 내부 함수
# 함수 안에 또 다른 함수를 정의할 수 있다.
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

# 내부 inner 함수는 루프나 코드 중복을 피하기 위해 또 다른 함수 내에 어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 사용된다.

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s' " % quote
    return inner(saying)

print(knights('Ni!'))

# 4.7.9 클로져
# 내부 함수는 클로져 closure 처럼 행동할 수 있다. 클로져는 다른 함수에 의해 동적으로 생성된다.
# 그리고 바깥 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수다.

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a)
print(b)

print(a())
print(b())

# 4.7.10 익명 함수: lambda()
# 파이썬 의 람다 함수 는 단일문으로 표현되는 익명 함수다.
def edit_story(words, func):
    '''
        words : words 리스트
        func: words 의 각 word 문자열에 적용되는 함수
    '''
    for word in words:
        print(func(word))

stairs = ['thudf', 'meow', 'thud', 'hiss']

def enliven(word):# 첫 글자를 대문자로 만들고 느낌표 붙이기
    return word.capitalize() + '!'

edit_story(stairs, enliven)

# 람다를 사용해서 enliven() 함수를 람다로 간단하게 바꿀 수 있다.
edit_story(stairs, lambda word: word.capitalize() + '!')

