# list = array 개념

import random as r # random 이라는 모듈을 import, r 로 사용.

# 빈 리스트 만드는 두가지 방법
a = []
b = list()

c = [1,2,3,4,5,6]

# 특정 범위의 int 값을 담는 list 만들기

d = list(range(0,10)) #0~9를 담는 list
print(d)

# 리스트의 slicing => list의 특정 범위만을 담은 새로운 list 반환.
print(c[0:5]) #[1,2,3,4,5]

#list의 합 => 두개의 리스트를 덧셈 순서대로 합친 새로운 list 반환

print(c+d) #[1,2,3,4,5,6,0,1,2,3,4,5,6,7,8,9]

# Append - list 끝에 새로운 item을 append => append(item) - Swift와 동일.
c.append(7)
print(c) #[1,2,3,4,5,6,7]

# Insert - list 특정 지점에 새로운 item을 insert
f = [1,2,3,4,5,7]
f.insert(5,6) #5번 index에 6을 insert

# Pop - attribute 없을때 : list 끝의 item을 없애기, attribute 있을때 : 해당 index의 item을 없애기.
f.pop()
print(f)
f.pop(2) #2번 index의 값 삭제
print(f) # [1,2,4,5,6]

# Remove - list에서 해당 값을 없애기.
f.remove(5) 
print(f) # [1,2,4,6]

# list에서 해당 item의 index를 반환하는 함수
print(f.index(1)) #0

# list의 item의 값을 모두 더해주는 함수 => sum(list)
print(sum(f)) #13

# list의 item중 최대/최소 값을 반환하는 함수 => max(list)/min(list)
print(max(f)) #13

#random 모듈을 import해서 사용할 수 있는 shuffle 함수 (여기서는 r로 사용) => list의 item 순서를 random하게 바꿔줌 (반환 x)
r.shuffle(f)
print(f)

#list의 값을 오름차순으로 정렬하는 함수 => sort()
f.sort()
print(f) #[1,2,4,6]
f.sort(reverse=True) #reverse=True로 sort 하면 역순(=내림차순 정렬)
print(f) #[6,4,2,1]

#list안의 모든 item 값을 없애는 함수 => clear()
f.clear()
print(f)

#list의 원소 수 (길이) 반환 하는 함수 => len(list)
f = [1,2,3,4,5]
print(len(f)) #5

# enumerate(list) : (item의 index : item) 형식의 튜플로 매칭하는 함수.
for i in enumerate(f):
    print(i)

# 참고 : Tuple vs List
'''
tuple도 서브스크립션을 통해 index로 요소 접근 할 수 있지만.
list의 item 값은 바꿀 수 있지만, tuple은 한번 선언하면, 내부의 item을 변경할 수 없다.
'''

# all / any : list의 모든 / 어떤 한가지 요소라도 특정 조건을 만족하는지 검사하는 함수.


if all(3>x for x in f) : # all 함수를 사용 => list f 안의 모든 원소 x가 조건을 만족해야함.
    print("3보다 크다")
else :
    print("3보다 작다") # 모든 원소들이 3>x를 만족하지 않기 때문에 "3보다 작다" 출력.

if any(3>x for x in f) : # any 함수를 사용 => list f 안의 모든 원소 x중 한개라도 조건을 만족해야함.
    print("3보다 크다") # 한개 이상의 원소가 조건을 만족하기 때문에 "3보다 크다" 출력.
else :
    print("3보다 작다") 