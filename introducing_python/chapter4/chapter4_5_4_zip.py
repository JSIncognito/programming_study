# zip() 함수를 사용해서 여러 시퀀스를 병렬로 순회하는 것
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'preach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# 어러 시퀀스 중 가장 짧은 시퀀스가 완료되면 zip() 은 멈춘다.
# 또한 zip() 함수로 여러 시쿼스를 순회하며, 동일한 오프셋에 있는 항목으로 튜플을 만들수 있다.
english = 'Monday', 'Tuesday', 'Wedneday'
french = 'Lundi', 'Mardi', 'Mercredi'
# 두 개의 튜플을 만들기 위해 zip() 을 사용한다. zip()에 의해 반환되는 값은 튜플이나 리스트 자신이 아니라 하나로 반환될 수 있는 순회 가능한 값이다.
print(list(zip(english, french)))
# zip() 의 결과를 dict() 에 넣기.
print(dict(zip(english, french)))
# 4.5.5. 숫자 시퀀스 생성하기 : range()
for x in range(0, 3):
    print(x)
print(list ( range(0, 3)))
# 거꾸로 진행하느 2 에서 0 의 숫자 시퀀스
for x in range(2, -1, -1):
    print(x)
print(list(range(2, -1, -1)))
# 0 에서 10 까지 2 칸씩 진행하는 짝수 리스트
print(list( range(0, 11, 2)))
