# 4.6 컴프리헨션
# 컴프리헨션 comprehension (함축) 은 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 콤팩트한 방법이다.

# 4.6.1 리스트 컴프리헨션
number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)

number_list = list(range(1, 6))
print(number_list)

# 리스트 컴프리헨션을 사용해서 리스트를 만드는 것이 조금 더 파이써닉한 방법이다.
# [표현식 for 항목 in 순회 가능한 객체]

# 리스트 컴프리헨션으로 정수 리스트만들기

number_list = [number for number in range(1, 6)]
print(number_list)

# 목록에 대한 값을 생성하는 첫 번째 number 변수가 필요하다. 이것은 루프의 결과를 number_list 변수에 넣어준다.
# 두 번째 number 변수는 for 문의 일부다.

# 첫 번째 number 변수를 보여주기 위한 예
number_list = [number-1 for number in range(1, 6)]
print(number_list)

# 리스트 컴프리헨션은 대괄호 ([]) 안에 루프가 있다.
# [표현식 for 항목 in 순회 가능한 객체 if 조건]

# 1과 5 사이에서 홀수 리스트 만들기
a_list = [number for number in range(1, 6) if number % 2 ==1]
print(a_list)

# 컴프리헨션에서 루프에 상응하는 하나 이상의 for.. 절을 사용할 수 있다.
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

# 컴프리헨션을 사용 (row, col) 튜플 리스트 cells 변수에 할당
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# 각 튜플로부터 row 와 col 의 값만 출력하기 위해 튜플언패킹 unpacking 을 할 수 있다.

for row, col in cells:
    print("unpacking : ", row, col)

# 4.6.2 딕셔너리 컴프리헨션

# {키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체}
# 리스트 컴프리헨션과 같이 딕셔너리 컴프리헨션 또한 if 테스트와 다중 for ... 절을 가질 수 있다.
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# 두 번째 예제
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}
print(letter_counts)
# set(word) 를 순회하는 것은 문자열 word 를 순회하는 것과 다르게 문자를 반환하기 때문에 다르게 동작한다.

# 4.6.3 셋 컴프리헨션
# {표현식 for 표현식 in 순회 가능한 객체}
a_set = {number for number in range(1, 6) if number % 3 == 1}
print("set : ",a_set)

# 4.6.4 제너레이터 컴프리헨션
# 튜플은 컴프리헨션이 없다.
number_thing = (number for number in range(1, 6))
# 괄호 안의 내용은 제너레이터 컴프리헨션 이다. 그리고 이것은 제너레이터 객체를 반환한다.
type(number_thing)

for number in number_thing :
    print(number)

number_list = list(number_thing)
print(number_list)
