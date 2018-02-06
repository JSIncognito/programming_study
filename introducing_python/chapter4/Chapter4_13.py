# 연습문제
# 4.13 연습문제
# 	4.1 guess_me 변수에 7을 할당한다.
#   그리고 값이 7 보다 작으면 문자열 'too low' 를, 7 보다 크면 'too high'를,
#   7과 같으면 'just right' 를 출력하는 조건 테스트(if, elif, else) 를 작성하라.
guess_me = 8
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print('too high')
else:
    print('just right')
# 	4.2 quess_me 변수에 7을 할당하고, start 변수에 1을 할당한다.
#   Start 와 quess_me 를 비교하는 while 문을 작성하라.
#   Start 가 guess_me 보다 작은 경우에는 'too low' 를 출력한다.
#   Start 와 guess_me 가 같은 경우에는 'found it!' 을 출력하고 루프를 종료한다.
#   Start 가 quess_me 보다 큰 경우에는 'oops' 를 출력하고 루프를 종료한다.
#   그리고 루프의 마지막에 start 를 1씩 증가시킨다.
guess_me = 7
start = 1
while True:
    if(start < guess_me):
        print('too low')
    elif(start == guess_me):
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1;

# 	4.3 for 문으로 리스트값 [3, 2, 1, 0] 을 출력하라.
number_list1 = []
for i in range(3, -1, -1):
    number_list1.append(i)
print(number_list1)

# 시퀀스 생성
print(list(range(3, -1, -1)))

# 컴프리헨션
number_list2 = [i for i in range(3, -1, -1)]
print(number_list2)

# 	4.4 리스트 컴프리헨션을 이용하여 range(10) 에서 짝수 리스트를 만들어라.
# [표현식 for 항목 in 순회 가능한 객체 if 조건]
number_list = [number for number in range(10) if number%2==0]
print(number_list)

# 	4.5 딕셔너리 컴프리헨션을 이용하여 squares 딕셔너리를 생성하라.
#   Range(10) 의 반환값을 키로 하고, 각 키의 제곱을 값으로 한다.
squares = {number: number**2 for number in range(10)}
print(squares.items())
print(squares.keys())
print(squares.values())

# 	4.6 셋 컴프리헨션을 이용하여 range(10) 에서 홀수 셋을 만들어라.
squares = {number for number in range(10) if number%2!=0}
print(squares)

# 	4.7 제너레이터 컴프리헨션을 이용하여 문자열 'Got ' 과 range(10) 의 각 숫자를 반환하라.
# 	For 문을 사용해서 제너레이터를 순회한다.
temp = ('Got %s'%number for number in range(10))
for t in temp:
    print(t)
# temp_list = list(temp)
# print(temp_list)

# 	4.8 ['Harry', 'Ron', 'Hermione'] 리스트를 반환하는 good 함수를 정의하라.
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 	4.9 range(10) 의 홀수를 반환하는 get_odds 제너레이터 함수를 정의하라. For 문으로 반환된 세 번째 홀수를 찾아서 출력하라.
def get_odds(first=0, last=10, step=1):
    number = first
    while number < last:
        if number%2!=0:
            yield number
        number += step

ranger = get_odds()
number = 0
for x in ranger:
    if(number == 2):
        print(x)
    number += 1

# 	4.10 어떤 함수 호출되면 'start' 를 , 끝나면 'end' 를 출력하는 test 데커레이터를 정의하라.
def test_document(func):
    def new_function(*arg, **kwargs):
        print("start: ", func.__name__)
        result = func(*arg, **kwargs)
        print("end:", result)
        return result
    return new_function

@test_document
def add_ints(a, b):
    return a + b

print(add_ints(1, 3))

# 	4.11 OopsException 이라는 예외를 정의하라. 이 예외를 발생시켜서 무슨 일이 일어나는지 살펴보라.
#   이 예외를 잡아서 'Caught an oops' 를 출력하는 코드를 작성하라.
class OopsException(Exception):
    print('Caught an oops')

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise OopsException(word)
        except OopsException as exc:
            print(exc)

# 	4.12 zip() 함수를 사용하여 다음 두 리스트를 짝으로 하는 movies 딕셔너리를 만들어라.
# 	Titles =['Creature of Habit', 'Crewel Fate']
#   Plote = ['A nun turns into a mon ster', 'A haunted yarn shop']
Titles = ['Creature of Habit', 'Crewel Fate']
Plote = ['A nun turns into a mon ster', 'A haunted yarn shop']

movies = {title: plote for title, plote in zip(Titles, Plote)}
print(movies)
print(movies.keys())
print(movies.values())