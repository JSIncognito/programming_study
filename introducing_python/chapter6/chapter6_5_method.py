class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()
#give_me_a_car.need_a_push()

# 6.7 자신 : self
car = Car()
car.exclaim()

# car 객체의 Car 클래스를 찾는다.
# car 객체를 Car 클래스의 exclaim() 메서드의 self 메개변수에 전달한다.

Car.exclaim(car)
