# 3.2.1 리스트 생성하기 : [] 또는 list ()
# 리스트는 0 혹은 그 이상의 요소로 만들어진다. 콤마(, ) 로 구분하고, 대괄호 ([]) 로 둘러싸여 있다.
empty_list = []
print(empty_list)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays)
big_birds = ['emu', 'ostrich', 'cassowary']
print(big_birds)
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
print(first_names)
# list() 함수로 빈 리스트를 할당할 수 있다.
another_empty_list = list()
print(another_empty_list)

# 리스트를 생성하는 다른 방법 리스트 컴프리헨션 list comprehension 이 있음...

# 3.2.2 다른 데이터 타입을 리스트로 변환하기 : list()
# list() 함수는 다른 데이터 타입을 리스트로 변환한다.
print(list('cat'))

# 튜플을 리스트로 변환
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# split() : split() 은 문자열을 구분자로 나누어서 리스트로 교환한다.
birthday = '1/6/1952'
print(birthday.split('/'))

# 3.2.3 [offset] 으로 항목 얻기
# 오프셋으로 하나의 특정 값을 추출할 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])

# 움수의 인덱스는 끝에서 거꾸로 값을 추출할 수 있다.
print(marxes[-1])

# 3.2.4 리스트의 리스트
# 리스트는 리스트뿐만 아니라 다른 타이브이 요소도 포함할 수 있다.
small_birds = ['hummingbird', 'finch']
extinch_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinch_birds, 'macaw', carol_birds]
print(all_birds)
# all_birds 첫 번째 항목을 추출
print(all_birds[0])
# 두 번째 항목을 추출
print(all_birds[1])
#extinct_birds 리스트의 첫 번째 항목을 all_birds 리스트에서 다음과 같이 두 인덱스를 사용해서 추출할 수 있다.
print(all_birds[1][0])

#3.2.5 [offset]으로 항목 바꾸기
# 오프셋으로 항목을 얻어서 바꿀 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
# 리스트의 오프셋은 리스트에서 유효한 위치여야 한다.