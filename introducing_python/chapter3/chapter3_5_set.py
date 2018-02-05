# 3.5.1 셋 생성하기 : set()
# 셋을 생성할 때는 다음과 같이 set() 함수 혹은 중괄호 ({}) 안에 콤마로 구분된 하나 이상의 값을 넣으면 도니다.
empty_set = set()
print("empty_set: ", empty_set, type(empty_set))

even_numbers = {0, 2, 4, 6, 8}
print("even_numbers : ",even_numbers, type(even_numbers))

odd_numbers = {1, 3, 5, 7, 9}
print("odd_numbers :", odd_numbers, type(odd_numbers))
# 딕셔너리의 키와 마찬가지로 셋은 순서가 없다.

# 3.5.2 데이터 타입 변환하기 : set()
# 리스트, 문자열, 튜플, 딕셔너리로부터 중복된 값을 버린 셋을 생성할 수 있다.

# 리스트를 셋으로
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# 튜플을 셋으로
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# 딕셔너리에 set() 을 사용하면 키만 사용한다.
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# 3.5.3 in 으로 값 멤버십 테스트하기
# 이것은 일반적으로 사용되는 셋의 용도다. drinks 라는 딕셔너리를 만들어 보자 . 각 키는 혼합 음료의 이름이고, 값은 음료에 필요한 재로들의 셋이다.
drinks = {
    'martini':{'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
# 중괄호 ({}) 가 두 번 둘러싸여 있지만, 셋은 값들의 시퀀스일 뿐이고, 딕셔너리는 하나 이상의 키: 값의 쌍으로 이루어져 있다.

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# 3.5.4 콤비네이션과 연산자
# 셋값의 콤비네이션 combination (조합) 을 확인해 보자.
# 셋 인터섹션 연산자 set intersection operatior (셋 교집합 연산자) 인 엠퍼샌드 (&) 를 사용해서 원하는 음료를 찾아보자.

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(" & vermouth orange juice :",name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# & 연산자와 intersection() 함수를 사용해서 인터섹션 intersection( 교집합: 양쪽 셋에 모두 들어 있는 멤버) 를 구해보자.
print("a & b : ",a & b)
print("intersection : ",a.intersection(b))
print("bruss & wruss: ", bruss & wruss)

# | 연산자와 union() 함수를 사용해서 유니온 union ( 합집합 : 각 셋의 멤버 모두) 를 구해보자
print("a | b : ", a|b)
print("a.union : ", a.union(b))

print("bruss | wruss", bruss | wruss)

# - 연산자와 difference() 를 사용해서 디퍼런스 difference( 차집합: 첫 번째 셋에는 있지만 두 번째 셋에는 없는 멤버) 를 구해보자.
print("a- b :",a - b)
print("a.difference(b): ", b)
print("bruss - wruss: ", bruss - wruss)
print("wruss - bruss: ", wruss - bruss)

# 일반적인 셋 연산의 유니온, 인터섹션, 디퍼런스를 외 다른 연산
# ^ 연산자나 symmetric_difference() 함수를 사용해서 익스클루시브 exclusive (대칭 차집합: 한 쪽 셋에는 들어 있지만 양쪽 모두에
# 들어 있지 않은 멤버) 를 구해보자

print("a ^ b: ", a^b)
print("a.symmetric_difference(b)", a.symmetric_difference(b))

print("bruss ^ wruss: ", bruss ^ wruss)

# <= 연산자나 issubset () 함수를 사용해서 첫 뻔째 셋이 두 번째 셋의 서브셋 subset (부분집합) 인지 살펴보자.
print("a <= b : ", a <= b)
print("a.issubset(b) : ", a.issubset(b))

print("bruss <= wruss : ", bruss <= wruss)

print("a <= a : ", a <= a, "a.issubset(a): ", a.issubset(a))

#첫 번째 셋이 두 번 째 셋의 프로퍼 서브셋 proper subset (진부분집합) 이 되려면,
## 두 번째 셋에는 첫 번째 셋의 모든 멤버를 포함한 그 이상의 멤버가 있어야 한다.
print("a<b : ", a<b, "a<a: ", a<a, "bruss<wruss: ", bruss<wruss)

# 슈퍼셋은 서브셋의 반대다. >= sk issuperset()  함수를 사용해서 첫 번째 셍이 두 번째 셋의 슈퍼셋인지 살펴보자.
print("a >= b : ", a>=b, "a.issuperset : ", a.issuperset(b), "wruss >= bruss", wruss >= bruss)

print("a >= a: ", a>=a, "a.issuperset(a) : ", a.issuperset(a))
# > 연산자를 사용해서 첫 번째 셋이 두 번째 셋의 프로퍼 슈퍼셋 proper superset 인지 확인해보자.
# 첫 번째 셋이 두 번째 셋의 프로퍼 슈퍼셋이 되려면, 첫 번째 셋에는 두 번째 세의 모든 멤버를 포함한 그 이상의 멤버가 있어야 한다.
print("a > b : ", a>b, "wruss > bruss: ", wruss > bruss, "a > a: ", a>a)