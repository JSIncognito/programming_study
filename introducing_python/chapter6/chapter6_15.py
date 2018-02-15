# 6.15 연습문제
# 6.1 아무 내용도 없는 Thing 클래스를 만들어서 출력하라.
# 그리고 이 클래스의 example 객체를 생성해서 출력하라.
# 두 출력값은 같은가?

class Thing():
    pass
print(Thing())
example = Thing()
print(example)
# 6.2 Thing2 클래스를 만들고, 이 클래스의 letters 속성에 값 'abc' 를 할당한 후 letters 를 출력하라.
class Thing2():
    def __init__(self, letters):
        self.letters = letters

thing2 = Thing2('abc')
print(thing2.letters)

# 6.3 Thing3 클래스를 만어라.
# 이번에는 인스턴스 (객체) 의 letters 속성에 값 'xyz' 를 할당한 후 letters 를 출력하라.
#  letters 를 출력하기 위해 객체를 생성해야 하는가?

class Thing3():
    letters = 'xyz'
    def __init__(self):
        pass

print(Thing3.letters)
# 6.4 name, symbol, number 인스턴스 속성을 가진 Element 클래스를 만들어라.
# 이 클래스로부터 'Hydrogen', 'H', 1 값을 가진 객체를 생성하라.

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def about(self):
        print(self.name, self.symbol, self.number)

element = Element('Hydrogen', 'H', 1)
element.about()
# 6.5 'name' : 'Hydrogen', 'symbol':'H', 'number':1 과 같이 키와 값으로 이루어진 el_dict 딕셔너리를 만들어라.
# 그리고 el_dict 딕셔너리로 부터 Element 클래스의 hydrogen 객체를 생성하라.
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.about()
# 6.6 Element 클래스에서 객체의 속성(name, symbol, number) 값을 출력하는 dump() 메서드를 정의하라.
# 이 클래스의 hydrogen 객체를 생성하고, dump() 메서드로 이 속성을 출력하라.
class Element2():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Element2('hun', 'J', '2')
hydrogen.dump()
# 6.7 print(hydrogen) 을 호출하라.
# Element클래스의 정의에서 dump 메서드를 __str__ 메서드로 바꿔서 새로운 hydrogen 객체를 생성하라.
# 그리고 print(hydrogen) 을 다시 호출해보라.
print(hydrogen)
class Element3:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return self.name + self.symbol + str(self.number)
        #print(self.name, self.symbol, self.number)

hydrogen = Element3('Yoo', 'Y', 3)
print(hydrogen)

# 6.8 Element 클래스를 수정해서 name, symbol, number 의 속성을 private 로 만들어라.
# 각 속성값을 반환하기 위해 getter 프로퍼티를 정의한다.
class Element4():
    def __init__(self, in_name, in_symbol, in_number):
        self.__name = in_name
        self.__symbol = in_symbol
        self.__number = in_number

    @property
    def name(self):
        print('name the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('name the setter')
        self.__name = input_name

    @property
    def symbol(self):
        print('symbol the getter')
        return self.__symbol

    @property
    def number(self):
        print('number the getter')
        return self.__number

temp = Element4('Jay', 'J', 5)
print(temp.name)
#print(temp.__name)

print('위치확인 123')
temp.name = 'Test'
print(temp.name)

# 6.9 세 클래스 Bear, Rabbit, Octothorpe 를 정의하라.
# 각 클래스에 eats() 메서드를 정의하라 각 메서드는 'berries'(Bear), 'clover' (Rabbit),
#  또는 'campers' (Octothorpe) 를 반환한다. 각 클래스의 객체를 생성하고 , eats() 메서드의 반환값을 출력하라.
class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octothorpe():
    def eats(self):
        return 'campers'

be = Bear()
ra = Rabbit()
oc = Octothorpe()

print(be.eats())
print(ra.eats())
print(oc.eats())
# 6.10 Laser, Claw, SmartPhone 클래스를 정의하라.
# 각 클래스는 does() 메서드를 갖고 있다.
# 각 메서드는 'disintegrate'(Laser), 'crush' (Claw), 또는 'ring' (Smart Phone) 을 반환한다.
# 그리고 각 인스턴스 (객체) 를 갖는 Robot 클래스를 정의하라.
# Robot 클래ㅢ 객체가 갖고 잇는 내용을 출력하능 dose() 메서드를 정의하라.
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        print('here __init ')
        self.laser = Laser()
        self.claw = Claw()
        self.smart = SmartPhone()
    def dose(self):
         return '''I have many attachments:
         laser, to %s. claw %s. smart %s.''' % (
             self.laser.does(), self.claw.does(), self.smart.does())

robbie = Robot()
print(robbie.dose())
