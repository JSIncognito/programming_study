# 3.4.1 딕셔너리 생성하기:{}
# 중괄호 ({}) 안에 콤마로 구분된 키:값 쌍을 지정한다. 키:값 쌍이 하나도 없는 빈 딕셔너리다.
empty_dict = {}
print("empty_dict: ", empty_dict, type(empty_dict))

bierce = {
    "day":"A period of twnty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

# 3.4.2 딕셔너리로 변환하기 : dict()
# dict () 함수를 사용해서 두 값으로 이루어진 시퀀스를 딕셔너리로 변환할 수 있다.

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print("dict lol : ",dict(lol))
# 각 시퀀스의 첫 번째 항목은 키로, 두 번째 항목은 값 으로 사용된다.

# 두 항목 튜플로 된 리스트
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print("dict lotuple :", dict(lot))

# 두 항목 리스트로 된 튜플
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print("dict tol: " , dict(tol))

# 두 문자 문자열로 된 리스트
los = ['ab', 'cd', 'ef']
print("dict los : ", dict(los))
# 두 문자 문자열로 된 튜플
tos = ('ab', 'cd', 'ef')
print("dict tos : ", dict(tos))
# '여러 시퀀스 수회하기 : zip ()' 에서는 zip () 함수로 두 항목 시퀀스를 쉽게 생성하는 방법을 알아본다.

# 3.4.3 항목 추가 / 변경하기 : [key]
# 영국의 희극단, 몬티 파이튼 Monty python 멤버의 성을 키 key 로 , 이름 값 value 으로 하는 딕셔너리
pythons ={
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print("변경하기 1",pythons)
# Terry 를 Gerry
pythons['Gilliam'] = 'Gerry'
print("변경하기 2",pythons)
pythons['Gilliam'] = 'Terry'
print("변경하기 3",pythons)

# 3.4.4 딕셔너리 결합하기 : update()
# update() 함수는 한 딕셔너리의 키와 값들을 복사해서 다른 딕셔너리에 붙여준다.
pythons = {
    'Chapman':'Graham',
    'Cleese': 'John',
    'Gilliam':'Terry',
    'Idel': 'Eric',
    'Jones':'Terry',
    'palin':'Michael',
}
print("update 1",pythons)
others = {'Marx':'Groucho', 'Howard':'Moe'}
pythons.update(others)
print("update 2: ", pythons)

first ={'a':1, 'b':2}
second = {'b':'platypus'}
first.update(second)
print(second)

# 3.4.5 키와 del 로 항목 삭제하기
del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)

# 3.4.6 모든 항목 삭제하기 : clear()
# 딕셔너리에 잇는 키와 값을 모두 삭제하기 위해서는 clear() 을 사용하거나 빈 딕셔너리 ({}) 를 이름에 할당한다.
pythons.clear()
print(pythons)

pythons = {}
print(pythons)

# 3.4.6 in 으로 키 멤버십 테스트하기
# 딕셔너리에 키가 존재하는지 알고 싶다면 in 을 사용한다.
pythons = {'Chapan': 'Graham', 'Cleese': 'John', 'Jones':'Terry', 'Palin':'Michael'}

print('Chapan' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

# 3.4.8 항목 얻기 :[key]
# 딕셔너리에서 가장 일반적인 용도. 딕셔너리에 키를 지정하여 상응하는 값을 얻는다.

print(pythons['Cleese'])

# 딕셔너리에 키가 존재하지 않으면 예외를 얻게 된다.
#print(pythons['Marx'])

# 이 문제를 피하는 좋은 방법
# 첫 번째 방법은 이전 절에서 본 in 으로 키에 대한 멤버십 membership 테스트를 실행하는 것
# 두 번째 방법은 딕셔너리의 get() 함수를 사용하는 것
# get() 함수는 딕셔너리, 키, 옵션값을 사용한다. 만약 키가 존재하면, 그 값을 얻는다.
print("get() Cleese :",pythons.get('Cleese'))

print("get() : ", pythons.get('Marx', 'Not a Pythons'))
# 옵션값을 지정하지 않으면 None 을 얻는다.
print(pythons.get('Marx'))

# 3.4.9 모든 키 얻기 : keys()
# 딕셔너리의 모든 키를 가져오기 위해서는 keys () 를 사용한다.
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())

# 3.4.10 모든 값 얻기 : values()
# 딕셔너리의 모든 값을 가져오기 위해서는 values() 를 사용한다.
print(list(signals.values()))

# 3.4.11 모든 쌍의 키 - 값 얻기 : items()
# 딕셔너리의 모든 쌍의 키와 값을 어기 위해서는 items () 를 사용한다.
print(signals.items())
# 각 키와 값은 튜플로 반환된다.

# 3.4 12 할당 : =, 복사 : copy ()
# 리스트와 마찬가지로 딕셔너리를 할당한 후 변경할 때 딕셔너리를 참조하는 모든 이름에 변경된 딕셔너리를 반영한다.
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print("save_signals 1: ",save_signals)

# 딕셔너리의 키와 값을 또 다른 딕셔너리로 복사하기 위해서는 위와 같이 할당하지 않고 copy() 를 사용한다.
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print("signals : ",save_signals)
print("original_signals:", original_signals)
