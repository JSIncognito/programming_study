# 4.5 순회하기 : for
# 파이썬에서 이터레이터 iterator 는 자주 유용하게 쓰인다. 자료구조가 얼마나 큰지, 어떻게 구현되었는지에 관계없이 자료구조를 순회할 수 있도록 해준다.
# 데이터 메모리에 맞이 낳더라도 데이터 스트림을 처리할 수 있도록 허용해준다.

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# 파이써닉한 방법
for rabbit in rabbits:
    print(rabbit)

# rabbitsㅇ 리스트는 문자열, 튜플, 딕셔너리, 셋 등과 같이 순회 가능한 iterable 객체다. 튜플이나 리스트는 한 번에 한 항목을 순회한다.

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'ewapon': 'lead pipe', 'person': 'Col. Mustard'}

for card in accusation: # 혹은 for card in accusation.keys():
    print(card)

# 키보다 값을 순회하려면 딕셔너리의 values() 함수를 사용
for value in accusation.values():
    print(value)

# 딕셔너리 에서 키와 값을 모두 반환하기 위해서는 items() 함수를 사용
for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# 4.5.3 break 확인하기 : else
# else 문은 break 문에 의해 반복문이 중단되었는지 확인 ...
cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print("this shop has some lovely", cheese)
    break
# else: # break 문이 호출되지 않았다면 cheeses 가 없는 것이다.
#     print("This is not much of a cheese shop, is it?")

if not found_one:
    print("this is not nuch of a cheese shop, is it?")
