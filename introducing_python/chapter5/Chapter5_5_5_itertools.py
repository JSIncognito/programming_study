# 5.5.5 코드 구조 순회하기 : itertools

# chain()
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print("chain : ",item)

# cycle()
for item in itertools.cycle([1, 2]):
    print("cycle :",item)
    if(item == 2): break

# accumulate()
for item in itertools.accumulate([1, 2, 3, 4]):
    print("total sum : ", item)

# 축적된 곲을 계산
def nultiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], nultiply):
    print(" a * b : ",item)

# 5.5.6 깔끔하게 출력하기 : pprint()
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'Awise quy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])

print("print : ",quotes)
pprint("pprint :",quotes)