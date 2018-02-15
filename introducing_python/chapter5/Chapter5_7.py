# 5.7 연습문제
# 	5.1 zoo.py 파일에서 'Open 9-5 daily' 문자열을 반환하는 hours() 함수를 정의하라.
#  그리고 나서 대화식 인터프리터에서 zoo 모듈을 임포트한 후 hours () 함수를 호출하라
import zoo
print(zoo.hours())
# 	5.2 대화식 인터프리터에서 zoo 모듈을 menagerie 라는 이름으로 임포트한 후 hours() 함수를 호출하라.
import zoo as menagerie
print(menagerie.hours())

# 	5.3 인터프리터에서 zoo 모듈로부터 직접 hours() 함수를 임포트해서 호출하라.
from zoo import hours
print(hours())

# 	5.4 hours () 함수를 info 라는 이름으로 임포트해서 호출하라.
from zoo import hours as info
print(info())

# 	5.5 키:값 쌍이 'a' :1, 'b' : 2 , 'c' : 3 인 plain 딕셔너리를 만들어서 출력하라.
plain = {'a': 1, 'b':2, 'c':3}
for p in plain:
    print(p)
# 	5.6 연습문제 5.5 의 plain 딕셔너리에 있는 키 : 값 쌍으로 fancy 라는 OrderedDict 를 만들어서 출력하라.
# Plain 딕셔너리와 출력 순서가 같은가?
from collections import OrderedDict
fancy = OrderedDict(plain)
for f in fancy:
    print(f)

# 	5.7 dict_of_lists 라는 defaultdict 를 만들어서 list 인자를 전달하라.
# 리스트 dict_of_lists['a] 에 'something for a ' 값을 추가하고, dict_of_lists['a']를 출력하라.
from collections import defaultdict
dict_of_lists = defaultdict(list)

dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])
print(dict_of_lists['b'])