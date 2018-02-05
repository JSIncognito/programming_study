# 3.3.1 튜플 생성하기:()
# () 튜플 생성하기
empty_tuple = ()
print("empty_tuple", empty_tuple)

# 하나 이상의 요소가 있는 튜플을 만들기 위해서는 각 요소 뒤에 콤사 ( , ) 를 붙인다.
one_marx = 'Groucho'
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
# 파이썬은 튜플을 출력할 때 괄호 () 를 포함한다. 튜플을 정의할 때는 괄호 () 가 필요 없다.
# 뒤에 콤마가 붙는다는 것은 튜플을 정의한다는 뜻이다.
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# 튜플은 한 번에 여러 변수를 할당할 수 있다.
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print("a: " ,a, type(a))
print("b: ", b, type(b))
print("c: ", c, type(c))
# list 동일
marx_list = ['Groucho', 'Chico', 'Harpo']
aa, bb, cc = marx_list
print("aa: ",aa, type(aa))
print("bb: ",bb)
print("cc: ",cc)

# 이것을 튜플 언패킹 tuple unpacking 이라고 부른다.
# 한 문장에서 값을 교환하기 위해 임시 변수를 사용하지 않고 튜플을 사용할 수 있다.

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print("password:", password)
print("icecream:", icecream)

#tuple() 은 다른 객체를 튜플로 만들어준다.
marx_list = ['Groucho', 'Chico', 'Harpo']
print("marx_list :",tuple(marx_list))