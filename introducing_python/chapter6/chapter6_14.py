from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)

print(duck.bill)
print(duck.tail)

parts ={'bill': 'wide orange', 'tail': 'long'}
#duck2 = Duck(bill = 'wide orange', tail = 'logn')
duck2 = Duck(**parts)
print(duck2)
# **parts 는 키워드 인자 keyword argument 다. parts 딕셔너리에서 키와 값을 추출하여 Duck() 의 인자로 제공한다.

# 네임드 튜플은 불변한다. 하지만 필드를 바꿔서 또 다른 네임드 튜플을 반환할 수 있다.
duck3 = duck2._replace(tail = 'magnificent', bill = 'crushing')
print(duck3)

# duck 을 딕셔너리로 정의한다.
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)

duck_dict['color'] = 'green'
print(duck_dict)

# 딕셔너리는 네이드 튜플이 아니다.
#duck_dict.color = 'green'
