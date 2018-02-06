# 4.4 반복하기 : while
# 파이썬에서 가장 간단한 루핑 메커니즘 while 문

# 1~5 까지 생성
count = 1
while count <= 5:
    print(count)
    count += 1

# input () 함수를 통해 키보드에서 한 라인을 읽은 후 첫 번째 문자를 대문자로 출력한다.
while True :
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

# 4.4.2 건너뛰기 : continue
# 정수가 홀수일 때는 그 수의 제곱을 출력하고, 짝수일 때는 다음 루프로 건너뛴다.

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)

# 4.4.3 break 확인하기 : else
# break 는 어떤 것을 체크하여 그것을 발견했을 경우 종료하는 while 문을 작성할 때 사용도니다.

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number", number)
        break;
    position += 1
else: # break 가 호출되지 않았다.
    print("No even number found")
