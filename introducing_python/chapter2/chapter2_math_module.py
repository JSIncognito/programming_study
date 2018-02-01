# page 470
# C.1.1 수학 함수
# 파이썬은 표준 math 모듈에서 다양한 수학 함수를 제공한다. import math 를 입력하여 함수에 접근할 수 있다.
# 수학 함수에는 pi 파이 와 e 자연상수 같은 상수도 포함되어 있다.
import math
print(math.pi)
print(math.e)
# 몇 가지 유용한 함수
# fabs() 함수는 인자의 절댓값을 반환한다.
a1=math.fabs(98.6)
print(a1)
a2=math.fabs(-271.1)
print(a2)
#floor() 함수는 내림 ceil() 함수는 올림하여 정수를 반환
b1=math.floor(98.6)
print("b1", b1)
b2=math.floor(-271.1)
print("b2", b2)
b3=math.ceil(98.6)
print("b3", b3)
b4=math.ceil(-271.1)
print("b4", b4)
# factorial() 함수를 사용하여 팩토리얼(n!) 을 계산한다.
f1 = math.factorial(0)
print("f1", f1)
f2 = math.factorial(1)
print("f2", f2)
f3 = math.factorial(2)
print("f3", f3)
f4 = math.factorial(3)
print("f4", f4)
f5 = math.factorial(10)
print("f5", f5)
# log() 함수로 밑 base 이 e 인 인자의 로그를 구한다.
e1 = math.log(1.0)
print("e1", e1)
e2 = math.log(math.e)
print("e2", e2)
# 로그의 밑을 다르게 하고 싶으면 두 번째 인자를 입력하면 된다.
e3 = math.log(8, 2)
print("e3", e3)
# pow() 함수는 수를 거듭제곱한다.
e4 = math.pow(2, 3)
print("e4", e4)
# 파ㅣ썬은 또한 같은 일을 수행하는 지수 연산자 ** 를 제공한다. 이 연산자는 밑과 거듭제곱의 수가 둘 다 정수인 경우 자동으로 부동소수점수로
# 변환되지 않는다.
# sqrt() 함수는 제곱근을 계산한다.
e5 = math.sqrt(100.0)
print("e5", e5)
# sin(), cos(), tan(), asin(), acos(), atan(), atan2() 하수와 같은 일반적인 삼각함수를 모두 제공한다.
x = 3.0
y = 4.0
xy = math.hypot(x, y)
print("xy", xy)
# hypot() 함수를 사용하여 두 수로부터 빗변의 길이를 구할 수 있다.
xy1 = math.sqrt(x*y + y*y)
xy2 = math.sqrt(x**2+y**2)
print("xy1:", xy1, "xy2:", xy2)
# radians() 함수는 각도의 좌표를 변환한다.
xy3 = math.radians(180.0)
pi = math.degrees(math.pi)
print("xy3", xy3, "pi:", pi)
