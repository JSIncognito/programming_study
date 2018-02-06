# 4.8 제너레이터 generator
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)

ranger = my_range(1, 5)
print(ranger)
for x in ranger:
    print(x)
