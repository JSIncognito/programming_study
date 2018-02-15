class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

# 자식 클래스에서 __init__() 메서드를 정의하면 부모 클래스의 __init__() 메서드를 대체하는 것이기 때문에 더 이상 자동으로
# 부모 클래스의 __init__() 메서드가 호출되지 않는다. 그러므로 이것을 명시적으로 호출해야한다.

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)

# 일반 Person 객체와 마찬가지로 Person 클래스를 활용하기 위해 super() 를 사용했다. super() 메서드 사용에 대한 또 다른 이점이 있다.
# 만약 Person 클래스의 정의가 나중에 바뀌면 Person 클래스로부터 상속받은 EmailPerson 클래스의 속성과 메서드에 변경사항이 반영된다.
