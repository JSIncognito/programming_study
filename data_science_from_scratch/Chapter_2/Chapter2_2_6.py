# 2.2.6 객체 지향 프로그래밍 Object Oriented Programming
# 만약 Set 클래스를 생성한다면? ?

# 클래스의 이름은 관습에 따라 파스칼케이스로 표기
class Set2:
    def __init__(self, values=None):
        """
        이것은 constructor (생성자) 이다
        새로운 Set 을 만들면 호출된다.
        다음과 같이 사용할 수 있다.

        s1 = Set() # 비어 있는 Set
        s2 = Set([1, 2, 2, 3]) # 초깃값이 주어진 Set
        :param values:
        """
        self.dict = {} # 모든 Set 의 인스턴스는 자체적으로 dict 를 유지한다.
        # 이 dict 를 통해 항목의 존재 여부를 확인할 것이다.

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """파이썬 프롬프트에서 이 함수를 입력하거나 set() 으로 보내 주면 Set 객체를 문자열로 표현해 줌 """
        return "Set: " + str(self.dict.keys())

    # self.dict 에서 항목과 True 를 각각 key 와 value 로 사용해서
    # Set 안에 존재하는 항목을 표현
    def add(self, value):
        self.dict[value] = True

    # 만약 항목이 dict 의 key 라면 항목은 Set 안에 존재함
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

# 클래스 활용
s = Set2([1, 2, 3])
print(s)
s.add(4)
print(s.contains(4))
s.remove(3)
print(s.contains(3))