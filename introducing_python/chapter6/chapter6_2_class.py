# 특별한 파이썬 객체 초리화 initialization 메서드 __init__ 정의
# __init__() 과 self 가 생소하다. __init__() 은 특별한 메서드 이름이다. 이 메서드는 클래스의 정의로부터 객체를 초기화한다.
# self 인자는 객체 자신을 가르킨다.

# 클래스에서 __init__() 을 정의할 때, 첫 번째 매개변수는 self 여야 한다. 비록 파이썬에서 self 는 예약어가 아니지만, 일반적으로
# 이렇게 사용한다.
class Person():
    """
    * Person 클래스의 정의를 찾는다.
    * 새 객체를 메모리에 초기화(생성) 한다.
    * 객체의 __init__ 메서드를 호출한다. 새롭게 생성된 객체를 self 에 전달하고, 인자 를 name 에 전달한다.
    """
    def __init__(self, name):
        self.name = name

# Person 객체 생성, 인자값 name 을 Elmer Fudd로 하여 생성한다.
hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)
# 새로운 객체는 파이썬의 다른 객체의 생성 과정과 같다. 이 객체는 리스트, 튜플, 딕셔너리, 또는 셍의 요소로 사용할 수 있다.
# 이 객체를 함수에 인자로 전달할 수 있고, 함수에서 그 결과를 반환할 수 있다.
# 우리가 전달한 name 값에 무엇이 있는지 살펴보자. 그것은 객체의 속성 attribute 에 저장되어 있다.

# Person 클래스 정의에서 name 속성을 self.name 으로 접근하는 것을 기억하라. hunter 와 같은 객체를 생설할 때,
# 이것을 hunter.name 이라 여긴다.

# 모든 클래스 정의에서 __init__ 메서드를 가질 필요는 없다. __init__ 메서드는 같은 클래스에서 생성된 다른 객체를 구분하기
# 위해 필요한 다른 뭔가를 수행한다.


