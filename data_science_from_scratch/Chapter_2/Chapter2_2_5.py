# 2.2.5 정규표현식
# 정규표현식 (regular expressions) , 또는 regex 를 사용하면 문자열을 찾을 수 있다.
# 간단한 예시
import re

print( all(([
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
])))
# 모두 True
# 'cat' 은 'a' 로 시작하지 않기 때문에
# 'cat'안에는 'a' 가 존재하기 때문에
# 'dog' 안에는 'c'가 존재하지 않기 때문에
#  a 혹은 b 기준으로 나누면
#  ['c', 'r', 's'] 가 생성되기 때문에
# 숫자를 "-" 로 대체 True 가 출력됨

