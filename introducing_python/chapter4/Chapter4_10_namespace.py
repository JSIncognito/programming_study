# 4.10 네임스페이스와 스코프
animal = 'fruitbat'
def print_flobal():
    print('inside print_global:', animal)

print('at the top level: ', animal)

# def change_and_print_global():
#     print('inside change_and_print_global: ', animal)
#     animal = 'wombat'
#     print('after the change:', animal)
#change_and_print_global()

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
print(animal)
print(id(animal))

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print("change_func befor :",animal)
change_and_print_global()
print("change_func after : ",animal)

animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())

print(animal)

change_local()

print('glovals:', globals())
print(animal)

# 4.10 이름에 _와 __사용
def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This fucntion is named: ', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()

