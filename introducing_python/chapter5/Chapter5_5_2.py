# 5.5.2 항목 세기:Counter()
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print("Counter : ",breakfast)

# most_common()
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

print(breakfast_counter)

# lunch list
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print("lunch : ", lunch_counter)

# + 연산자를 사용해서 두 카운터를 결합할 수 있다.
print(breakfast_counter + lunch_counter)

# - 연산자를 사용해서 한 카운터에서 다른 카운터를 뺄 수 있다.
print("breakfast - lunch:", breakfast_counter - lunch_counter)

print("lunch - breakfast :",lunch_counter - breakfast_counter)

# set 과 마찬가지로, 인터섹션 연산자& 를 사용해서 공통된 항목을 얻을 수 있다.
print(breakfast_counter & lunch_counter)

# 유니온 연산자 | 을 사용하면 모든 항목을 얻을 수 잇다.
print(lunch_counter | breakfast_counter)

# 5.5.3 키 정렬하기 : OrderedDict()
# 딕셔너리의 키 순서는 예측할 수 없다는 것을 봤다. OrderedDict() 함수는 키의 추가 순서를 기억하고, 이터레이터로부터 순서대로
# 키값을 반환 한다.
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry' : 'Ow!',
    'Curly': 'Nyuk nyuk!',
}

for stooge in quotes:
    print(stooge)

# OrderedDict()
from collections import OrderedDict
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry' : 'Ow!',
    'Curly': 'Nyuk nyuk!',
}

for stooge in quotes:
    print("Ordered Dict : ",stooge)
    
# 5.5.4 스택 + 큐 == 데크
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))