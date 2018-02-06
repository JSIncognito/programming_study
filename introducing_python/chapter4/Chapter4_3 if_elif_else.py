# 4.3 비교하기 : if, elif, else
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's human, Or a hairlee bear.")

color = "puce"
if color == 'red':
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color =="bee purple":
    print("I don't know what it is, bout only bees can see it")

else:
    print("I've naever heard of the color", color)

# 동시에 여러 개의 식을 비교해야 한다면 최종 부울값을 판단하기 위해 and, or, not 오ㅓㅏ 같은 부울 연산자를 사용할 수 있다.
x = 7
print((5 < x) and (x < 10))
print((5 < x) or (x < 10))
print((5 < x) and (x > 10))
print((5 < x) and not (x > 10))

# 파이썬에서는 하나의 변수를 다음과 같이 여러 번 비교하는 것을 허용한다.
print((5 < x < 10))

print(5<x<10<999)

# 데이터 자료구자가  False 조건인지 확인하기 위해 진실 혹은 거짓의 정의를 사용한다.
some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empry!")
