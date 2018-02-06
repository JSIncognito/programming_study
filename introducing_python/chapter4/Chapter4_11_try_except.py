# 4.11 에러 처리하기 : try, except
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and ', len(short_list)-1, ' but got', position)


# 예외 타입을 넘어 예외 사항에 대한 세부정보를 얻고 싶다면 다음과 같이 변수 이름에서 예외객체 전체를 얻을 수 있다.
# except 예외 타입 as 이름

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit?]')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)

# try:
#     raise UopsException('panic')
# except UopsException as exc:
#     print(exc)
#
# print(panic)