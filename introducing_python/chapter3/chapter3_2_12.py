# 3.2.12 오프셋으로 항목을 얻은 후 삭제하기: pop()
# pop() 은 리스트에서 항목을 가져오는 동시에 그 항목을 삭제한다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print("pop 이후 :",marxes)
print(marxes.pop(1))
print('pop(1) 이후 : ', marxes)

# 3.2.13 값으로 항목 오프셋 찾기 : index()
# 항목 값의 리스트 오프셋을 알고 싶다면 index() 를 사용한다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

#3.2.14 존재여부 확인하기 : in
# 리스트에서 어떤 값의 존재를 확인하려면 in을 사용
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)
# 리스트에 같은 값이 여러개 존재할 경우, 적어도 하나 이상 존재하면 in은 True 를 반환한다.

# 3.2.15 값 세기: count()
# 리스트에 특정 값이 얼마나 있는지 세기 위해서는 count() 를 사용한다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print("count : ", marxes.count('Harpo'))
print("count : ", marxes.count('Bob'))

# 3.2.16 문자열로 변환하기: join()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(', '.join(marxes))

# 어떤 반복 가능한 타입을 처리하기 위해 각 타입을 실제로 병합할 수 있도록 처리 하는 방법
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print("join: ", joined)

separator = joined.split(separator)
print("split:",separator)
print(separator == friends)