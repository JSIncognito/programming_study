# 파이썬 표준 라이브러리
# 제네릭을 사용할 수 있는 일부 모듈

# 5.5.1 누락된 키 처리하기 : setdefault(), defaultdict()

periodic_table = {'Hydrogen':  1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)


helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)


# defaultdict()
from collections import defaultdict
periodic_table = defaultdict(int)

print(periodic_table)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table)

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

# lamda 를 사용하여 인자에 기본값을 만드는 함수를 정의할 수 있다.
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

# 카운터를 만들기 위해 아래와 같이 int 함수를 사용할 수 있다.
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

print(food_counter)

for food, count in food_counter.items():
    print(food, count)

# 이전 예제에서 food_dounter 딕셔너리가 defaultdict 가 아닌 일반 딕셔너리였다면, 파이썬은
# 딕셔너리 요소의 food_counter[food] 를 증가시키려고 할 때마다 예외를 발생시킨다. 딕셔너리가 초기화 되지 않았기 때문이다.
# 예외를 피하려면 다음과 같은 추가 작업이 필요하다
dict_counter = {}

for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)
