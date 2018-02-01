# 3.2.6 슬라이스로 항목 추출하기
# 슬라이스를 사용해서 리스트의 서브시퀀스를 추출할 수 잇다.
marxes = ['Grouch', 'Chico', 'Harpo']
print(marxes[0:2])
# 리스트의 슬라이스 또한 리스트다.
# 처음부터 오른쪽으로 2칸씩 항목을 추출
print(marxes[::2])
# 끝에서 왼쪽으로 2칸씩 항목을 추출
print(marxes[::-2])
# 리스트 반전
print(marxes[::-1])
# 3.2.7 리스트의 끝에 항목 추가하기: append()
# append() 는 리스트의 끝에 새 항목을 추가한다.
marxes.append('Zeppo')
print("marxes append: ", marxes)
# 3.2.8 리스트 병합하기 : extend() 또는 +=
# extend() 를 사용하여 리스트를 병합할 수 있다. 리스트 marxes 에 새로운 리스트 others 를 병합
others= ['Gummo', 'Karl']
marxes.extend(others)
print("extend : ", marxes)
# += 로 합치기
marxes = ['Grouch', 'Chico', 'Harpo', 'Zeppo']
others= ['Gummo', 'Karl']
marxes += others
print("+= :", marxes)
# append() 를 사용하면 항목을 병합하지 않고, others 가 하나의 리스트로 추가된다.
marxes = ['Grouch', 'Chico', 'Harpo', 'Zeppo']
others= ['Gummo', 'Karl']
marxes.append(others)
print("append(): ", marxes)
# 3.2.9 오프셋과 insert() 로 항목 추가하기
# insert () 함수는 원하는 위치에 항목을 추가할 수 있다.
marxes.insert(3, 'Gummo')
print("insert:",marxes)
marxes.insert(10, 'Karl')
print("insert: ",marxes)
# 3.2.10 오프셋으로 항목 삭제하기 : del
del marxes[-1]
print("del",marxes)

marxes = ['Grouch', 'Chico', 'Harpo', 'Gummo','Zeppo']
print(marxes[2])
del marxes[2]
print(marxes)
print(marxes[2])
# 3.2.11 값으로 항목 삭제하기 : remove()
# 리스트에서 삭제할 항목의 위치를 모르는 경우, remove() 와 값으로 그 항목을 삭제할 수 있다.
marxes = ['Grouch', 'Chico', 'Harpo', 'Gummo','Zeppo']
marxes.remove('Gummo')
print("remove: ", marxes)

