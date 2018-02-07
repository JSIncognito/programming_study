#2.2.8 enumerate
# list 를 반복하면서 list 의 항목과 인덱스가 모두 필요한 경우가 종종 있다.
document = ['body', 'foo', 'bar']

# 가장 파이썬스러운 방법은 (인덱스, 항목) 형태의 tuple 을 생성해 주는 enumerate 를 활용하는 것
for i, document in enumerate(document):
    do_something = (i, document)
    print(do_something)

# 만약 인덱스만 필요하다면 다음과 같이 코드를 작성할 수 있다.
for i in range(len(document)): do_something(i)
for i, _ in enumerate(document): do_something(i)

#앞으로 enumerate 를 자주 사용할 것이다.