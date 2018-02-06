# 4.9 데커레이터
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running funtion:', func.__name__)
        print("positional arguments: ", args)
        print("Keyword arguments: ", kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

@document_it
def add_ints2(a, b):
    return a+b

add_ints2(3, 5)

# 함수는 여러 개의 데커레이터를 가질 수 있다.
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints3(a, b):
    return a + b

add_ints3(3, 5)

@square_it
@document_it
def add_ints3(a, b):
    return a + b

add_ints3(3, 5)