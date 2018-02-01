# 3.2.17 정렬하기 : sort()
# 값을 이용하여 리스트를 정렬할 때 사용하는 방법

#sort() 는 리스트 자체를 내부적으로 정렬
#sorted() 는 리스트의 정렬된 복사본을 반환한다.

marxes =['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)

print("sorted 이후 marxes:",marxes)

marxes.sort()
print("sort 이후 amrxes:",marxes)

marxes.sort(reverse=True)
print("sort 내림차순 : ", marxes)

# 3.2.18 항목 개수 얻기 : len()
# len () 은 리스트의 항목 수를 반환
marxes =['Groucho', 'Chico', 'Harpo']
print("len : ", len(marxes))

# 3.2.19 할당: =, 복사 : copy()
# 리스트를 변수 두 곳에 할당했을 경우, 한 리스트를 변경하면 다른 리스트도 따라서 변경된다.
a = [1, 2, 3]
print("a:", a)
b = a
print("b:", b)
a[0] = 'surpise'
print("a and b: ",a, b)

# 새로운 리스트로 복사 copy() 함수 , list() 변환 함수, 슬라이스[:]
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print("a: ", a)
print("b: ", b, "c: ", c, "d: ", d)
