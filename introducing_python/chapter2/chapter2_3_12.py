# 2.3.12 대소문자와 배치
setup = 'a duck goes into a bar...'
# 양끝에서 . 시퀀스를 삭제한다.
print(setup.strip('.'))
# 첫 번째 단어를 대문자로 만든다.
print(setup.capitalize())
# 모든 단어의 첫 글자를 대문자로 만든다.
print(setup.title())
# 글자를 모두 대문자로 만든다.
print(setup.upper())
# 글자를 모두 소문자로 만든다.
print(setup.lower())
# 대문자는 소문자로, 소문자는 대문자로 만든다.
print(setup.swapcase())

### 문자열 정렬
# 문자열을 지정한 공간에서 중앙에 배치
print(setup.center(30))
# 왼쪽에 배치
print(setup.ljust(30))
# 오른쪽 배치
print(setup.rjust(30))

# 2.3.13 대체하기: replace()
print(setup.replace('duck', 'marmoset'))

# 100 회 까지 바꾼다.
print(setup.replace('a ', 'a famous ', 100))

# 주의사항 다른 단어의 중간 들어 있는 a 도 바뀔수 있음....
print(setup.replace('a', 'a famous ', 100))

# 대체하고 싶은 문자열이 전체 단어인지, 한 단어의 시작의 일부인지 등의 특수한 조건이 있다면, 정규표현식 reqular expression 을 사용하면 된다.