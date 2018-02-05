# 3.6 자료구조 비교하기
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}

print("marx_list[2] : ",marx_list[2], "marx_tuple[2] : ",marx_tuple[2])
print("marx_dict['Harpo'] : ", marx_dict['Harpo'])
# 3.7 자료구조를 더 크게
# 내장된 자료구조를 결합해서 더 크고 복잡한 자료구조를 만들 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
# 튜플의 각 요소는 리스트다.
tuple_of_lists = marxes, pythons, stooges
print("tuple_of_lists : ",tuple_of_lists)
# 세 리스트를 한 리스트에 포함 시킬 수 있다.
list_of_lists = [marxes, pythons, stooges]
print("list_of_lists : ", list_of_lists)
# 리스트의 딕셔너리르 만들어 보자
dict_of_lists = {'Marxes':marxes, 'Pythons': pythons, 'Stooges': stooges}
print("dict_of_lists : ", dict_of_lists)
# 제안사항이 있다면 데이터 타입 그 자체다. 딕셔너리의 키는 불변하기 때문에 리스트, 딕셔너리, 셋은 다른 딕셔너리의 키가 될 수 없다.
# 그러나 튜플은 딕셔너리의 키가 될 수 있다.
houses = {
    (44, 79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House'
}
print("houses :" , houses)