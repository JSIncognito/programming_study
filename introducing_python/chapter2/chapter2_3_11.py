# 2.3.11 문자열 다루기
# 뉴캐슬 공작부인의 불멸의 시 'What Is Liquid'
poem = '''All that doth flow we cannot liquid name 
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out 
But 'tis the wet that makes it die, no doubt.'''
# 처음 13 자를 출력 (오프셋 0 에서 12)
print(poem[:13])
# (스페이스와 줄바꿈을 포함해서) 이 시는 몇 글자로 되어 있는지 확인
print(len(poem))
# 이 시는 All 로 시작하는지 확인
print(poem.startswith('All'))
# 이 시는 That's all, folks ! 로 끝나는지 확인
print(poem.endswith('That\'s all, folks!'))
# 이 시에서 첫 번째로 the 가 나오는 오프셋 위치 확인
word = 'the'
print(poem.find(word))
# 마지막으로 the 가 나오는 오프셋 위치 확인
print(poem.rfind(word))
# 세 글자 the 가 몇 번 나오는지 확인
print(poem.count(word))
# 시는 글자와 숫자로만 이루어져 있는지 확인
print(poem.isalnum())