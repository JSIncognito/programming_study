# 3.8 연습문제
# 리스트, 튜플, 딕셔너리, 셋과 같은 자료구조를 배웠다. 2장에서 배운 숫자와 문자열, 자료구조를 활용하면 현실세계의
# 다양한 것을 표현할 수 있다.

# 3.1 출생년도에 대한 리스트 year_lists 를 만들어라. 출생년도를 첫 번째 요소로 하고 1년씩 증가하는 다섯 번째
# 생일까지의 요소를 넣는다. 출생년도가 1980이라고 가정한다.
year_lists = []
for i in range(1980, 1985):
    year_lists.append(i)
print("year_lists : ", year_lists)

# range(a, b) 라면, a 이상 b 미만의 범위를 의미한다.

# 3.2 years_list 의 세 번째 생일의 년도는 ? 참고로 오프셋 0 은 출생년도다.
print("year_lists 세 번째 생일의 연도 : ", year_lists[2])
# 3.3 years_list 중 가장 나이가 많을 때의 년도는?
print(min(year_lists))

# 3.4 things 리스트를 만들어라. 이 리스트는 "mozzarella", "cinderella", "salmonella" 세 문자열을 요소로 갖는다.
things = ["mozzarella", "cinderella", "salmonella"]
print("things List : ", things)

# 3.5 things 리스트에서 사람 이름의 첫 글자를 대문자로 바꿔서 출력하라. 그러면 리스트의 요소가 변경되나?
print(things[1].title())
# 3.6 things 리스트의 치즈 요소를 모두 대문자로 바꿔서 출력하라.
print(things[2].upper())
# 3.7 things 리스트에 질병 요소가 있다면 제거한 뒤 리스트를 출력하라.
things.remove('salmonella')
print("3.7 질병 요소 제거 : ",things)

# 3.8 surprise 리스트를 생성하라. 이 리스트는 "Groucho", "Chico", "Harpo" 세 문자열을 요소로 갖는다.
surprise = ["Groucho", "Chico", "Harpo"]
print("surprise : ", surprise)
# 3.9 surprise 리스트의 마지막 요소를 소문자로 변경하고, 단어를 역전시킨 후 , 첫 글자를 대문자로 바꿔라.

# python 문자열을 거꾸로 출력하는 방법
# 1. 문자열을 하나씩 반대로 잘라서 다시 입력시킨후 출력하는 방법
# 2. Reverse() 를 이용하는 방법
print(surprise[-1].lower()[::-1].title())
print(''.join(reversed(surprise[-1].lower())).title())

# 3.10 영어 - 프랑스어 사전을 의미하는 f2e 딕셔너리를 만들어라. 영어의 dog 는 프랑스어 cchien 이고, cat 은 chat, walrus 는 morse다.
# 딕셔너리를 출력해보라.
f2e_dict = {'dog':'chien', 'cat': 'chat', 'walrus': 'morse'}
print("dict :", f2e_dict)

# 3.11 f2e 딕셔너리에서 영어 walrus 를 프랑스어로 출력하라.
print(f2e_dict['walrus'])
# 3.12 영어 - 프랑스어 사전의 f2e 딕셔너리를 이용해서 프랑스어-영어 사전 e2f 딕셔너리를 만들어라(items 메서드 사용).
print(f2e_dict.items())
e2f=dict()
for f2e in f2e_dict.items():
    e2f.update({f2e[1]:f2e[0]})

print('e2f to f2e : ', e2f)
# 딕셔너리 결합하기 : update()

# 3.13 f2e 딕셔너리를 사용해서 프랑스어 chien 을 의미하는 영어를 출력하라.
for key, val in f2e_dict.items():
    if val == 'chien':
        print("chien e_key : ",key)
# 3.14 e2f 딕셔너리의 영어 단어 키를 출력하라.
print("e2f dict e_key : ",e2f.keys())
# 3.15 이차원 딕셔너리 life 를 만들어라. 최상위 키는 'animals', 'plants', 'other' 다, 그리고 'animals' 는 각각 'cats',
# 'octopi', ''emus' 를 키로 하고, 'henri', 'Grumpy', 'Lucy' 를 값으로 하는 또 다른 딕셔너리를 참조하고 있다. 나머지 요소는
# 빈 딕셔너리를 참조한다.
life = {'animals':{'cats':'henri', 'octopi':'Grumpy', 'emus':'Lucy'},'plants':{}, 'other':{}}
print(life)
# 3.16 life 딕셔너리의 최상위 키를 출력하라.
print(life.keys())
# 3.17 life['animals'] 의 모든 키를 출력하라.
print(life['animals'].keys())
# 3.18 life['animals']['cats'] 의 모든 값을 출력하라.
print(life['animals']['cats'])