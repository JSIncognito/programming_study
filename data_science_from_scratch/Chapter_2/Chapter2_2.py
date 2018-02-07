# 2.2.2 List Comprehension
# 기존의 list 에서 특정 항목을 선택하거나 변환시킨 결과를 새로우 list 에 저장해야 하는 경우도 자주 발생한다.
# 가장 파이썬스럽게 처리하는 방법은 list compre-hension 이다

even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)

squares = [x * x for x in range(5)]
print(squares)

even_squares = [x * x for x in even_numbers]
print(even_squares)

# 또한 dict 나 set 으로 변환 시킬 수 있다.
square_dict = { x : x * x for x in range(5)}
print(square_dict.items())

square_set = {x * x for x in [1, -1]}
print(square_set)
# 보통 list 에서 불필요한 값은 밑줄로 표기한다.
zeroes = [0 for _ in even_numbers]
print(zeroes)

# List comprehension 에는 여러 for 를 포함할 수 있고,

pairs = [(x, y)
         for x in range(10)
         for y in range(10)] # (0,0) (0,1) ... (9, 8), (9, 9)

print("pairs : ", pairs)
# 뒤에 나오는 for 는 앞에 나온 결과에 대해 반복한다.
increasing_pairs = [(x, y)                     # x< y 인 경우만 해당
                    for x in range(10)         # rnage(lo, hi) 는
                    for y in range(x + 1, 10)] # [lo, lo + 1, ..., hi - 1] 을 의미함
print("increasing_pairs : ", increasing_pairs)

# Generator 와 iterator
# 크기가 빠르게 증가한다는 것은 list 의 단점 중 하나이다. 실제로 range(1000000) 은 100만 개의 항목으로 구성된 list 를 만들어 준다.
# 하지만 한 번에 항목을 하나씩 처리하기 위해 list 전체를 사용하는 것은 엄청나게 비효율적이며 컴퓨터의 메모리가 부족해질 수 있다.
# 만약 list 앞부분의 몇몇 값만 필요하다면 list 전체를 계산할 필요가 없다.

# Generator(생성자) 는 (주로 for 문을 통해서) 반복할 수 있으며, generator 의 각 항목은 필요한 순간에 그때 그때 생성된다.
# Generator 을 만드는 한 가지 방법은 함수와 yield 를 활용하는 것이다.

def lazy_range(n):
    """range 와 똑같은 기능을 하는 generator"""
    i = 0
    while i < n :
        yield i
        i += 1

# 반복문은 yield 로 반환되는 값이 없을 때까지 반환된 값을 차례로 하나씩 사용한다.

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# 앞으로 generator 을 통해 각각의 key 와 value 를 한 번씩만 살펴보는 iteritems() 메서드를 더 자주 사용할 것이다.


# 2.2.4 난수 생성
# 데이터 과학을 하다 보면 난수(random number) 를 생성해야 할 때가 자주 있다. 이때 random 모듈을 사용할 수 있다.

import random

four_uniform_randoms = [random.random()for _ in range(4)]
print(four_uniform_randoms)

# 만약 동일한 난수를 계속 사용하고 싶다면 random.seed 를 통해 매번 고정된 난수를 생성하면 된다.

random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

# 인자가 1 개 혹은 2개인 random.randrange 메서드를 사용하면 range() 에 해당 하는 구간 안에서 난수를 생성할 수 있다.
random.randrange(10)
print("range(10) = [ 0, 1, .... ,9 ] 난수 생성 :",random.random())
random.randrange(3, 6)
print("range(3, 6) = [3, 4, 5] 난수 생성 : ",random.random())

# random 모듈에는 가끔씩 사용하지만 유요한 여러 함수가 존재한다. random.shuffle 은 list 의 항목을 임의 순서로 재정렬해 준다.
up_to_ten = [i for i in range(10)]
random.shuffle(up_to_ten)
print(up_to_ten)

# random.choice 메서드를 사용하면 list 에서 임의의 항목을 하나 선택할 수 있다.
my_best_friend = random.choice(['Alice', 'Bob', 'Charlie'])
print(my_best_friend)

# random.sample 를 사용하면 list 에서 중복이 허영되지 않는 임의의 표본 list 를 만들 수 있다.
lottery_numbers = [i for i in range(60)]
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

# 만약 중복이 허용되는 임의의 표본 list 를 만드록 싶다면 random.choice 메서드를 여러 번 사용하면 된다.
for_with_replacement = [random.choice(range(10))
                        for _ in range(4)]
print(for_with_replacement)