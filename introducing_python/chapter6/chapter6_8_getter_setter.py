class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howrd')
fowl.name

print(fowl.get_name())

fowl.name = 'Daffy'
print(fowl.name)

fowl.set_name('Daffy')
print(fowl.name)

# 프로퍼티를 정의하는 또 다른 방법은 데커레이터를 사용하는 것이다. 다음 예제는 두 개의 다른 메서드를 정의한다.
# 각 메서드는 name() 이지만, 서로 다른 데커레이터를 사용한다.

# getter 메서드 앞에 @property 데커레이터를 쓴다.
# setter 메서드 앞에 @property 데커레이터를 쓴다.

class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck2('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

# 이전 예제에서 객체에 저장된 속성 (hidden_name) 을 참조하기 위해 name 프로퍼티를 사용했다. 프로퍼티는 계산된 값을 참조할 수  있다.
# radius 속성과 계산된 diameter 프로퍼티를 가진 circle 클래스를 정의해보자.

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

# 속성에 대한 setter 프로퍼티를 명시하지 않는다면 외부로부터 이 속성을 설정할 수 없다. 이것은 입력  전용 read-only 속성이다.
# c.diameter = 20