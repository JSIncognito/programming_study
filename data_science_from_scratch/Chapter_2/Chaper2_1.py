# 2.1.6 함수
# docstring 함수 몸체 시작 부분에 문자열을 포함시켜 함수 정의에 문서를 붙일 수 있다.
def double(x):
    """
    이 곳은 함수에 대한 설명을 적어 놓는 공간이다.
    docstring 함수 몸체 시작 부분에 문자열을 포함시켜 함수 정의에 문서를 붙일 수 있다.
    예를 들어, "이 함수는 입력된 변수에 2를 곱한 값을 출력해 준다"
    :param x:
    :return:
    """
    return x*2

# 파이썬 함수들은 변수로 할당되거나 함수의 인자로 전달할 수 있다는 점에서 일급 함수(first-class) 의 특성을 가진다.
def apply_to_one(f):
    """
    인자가 1인 함수 f를 호출
    :param f:
    :return:
    """
    return f(1)

my_double = double
x = apply_to_one(my_double)
print(x)

# 익명의 람다 함수(lambda function) 도 간편하게 만들 수 있다.
y = apply_to_one(lambda x: x + 4)
print(y)

another_double = lambda  x: 2 * x
def another_double(x): return 2 * x

# 함수 인자에는 기본값을 할당할 수 있다. 기본값 외의 값을 전달할고 싶을 때는 값을 직접 명시해 주면 된다.
def my_print(message="my default message"):
    print(message)

my_print("hello")
my_print()

# 가끔씩 인자의 이름을 명시해 주면 편리하다.
def subtract(a=0, b=0):
    return a - b

subtract(10, 5)
subtract(0, 5)
subtract(b=5)

# 2.1.10 dict
# dict(dictionary, 사전) 는 파있너의 또 다른 기본적인 뎅티ㅓ 구조이며, 특정 value(값) 와 연고나된 key 를 연결해 주고 이를 사용해
# value 를 빠르게 검색할 수 있다.

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel" : 80, "Tim" : 95}

# 대괄호를 사용해서 key 의 value 를 불러올 수 있다.
joels_grade = grades["Joel"]
print(joels_grade)

# 존재 하지 않는 key 를 입력하면 KeyError 가 발생
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# 연산자 in 을 사용하면 key 의 존재 여부를 확인할 수 있다.
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

# dict 에서 get 메서드를 사용하면 입력한 key 가 dic 에 없어도 에러를 반환하기 않고
# 기본 값을 반환해 준다.
joels_grade = grades.get("Joel", 0)
ketes_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

# 또한 대괄호를 사용해서 key 와 value 를 새로 지정해 줄 수 있다.
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

# 정형화된 데이터를 간단하게 나타낼 때는 주로 dict 가 사용된다.
tweet = {
    "user":"joelgrus",
    "text" :  "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# list 에서 in 을 사용하기 때문에 느림
# dict 에서 in 을 사용하기 때문에 빠름
tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

"user" in tweet_keys # list 에서 in 을 사용하기 때문에 느림
"user" in tweet # dict 에서 in 을 사용하기 때문에 빠름
"joelgrus" in tweet_values

# dict 의 key 는 수정할 수 없으며 list를 key 로 사용할 수 없다. 만약 다양한 값으로 구성된 key 가 필요하다면 tuple 이나 문자열을
# key 로 사용하도록 하자

# defaultdict
# 문서에서 단어의 빈도수를 세어 보는 중이라고 상상해보자.

from collections import defaultdict
document = "Test Defaultdict"
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
print(dd_list)
dd_list[2].append(1)
print(dd_list.items())

dd_dict = defaultdict(dict)
dd_dict["Jel"]["City"] = "Seattle"
print(dd_dict.items())

dd_pair = defaultdict(lambda : [0, 0])
print(dd_pair.items())
dd_pair[2][1]= 1
print(dd_pair.items())
# 만약 key 를 사용해서 어떤 결과를 수집하는 중이라면 매번 key 가 존재하는지 확인할 필요없이 dict 를 생성할 수 있다.

# Counter
# Counter 는 연속된 값을 defaultdict(int) 와 유사한 객체로 변환해 주며, key 와 value 의 빈도를 연결시켜 준다.
# 아프로 히스토그램을 그릴 때 자주 사용할 것이다.

from collections import Counter
c = Counter([0, 1, 2, 0])
print(c)
word_counts = Counter(document)
print(word_counts)

# Counter 객체에는 굉장히 유용하게 쓰이는 most_common 함수가 있다

# 가장 자주 나오는 단어 10개와 이 단어들의 빈도수를 출력
for word, count in word_counts.most_common(10):
    print(word, count)