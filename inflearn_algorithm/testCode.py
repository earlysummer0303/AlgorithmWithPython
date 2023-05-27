'''
print("0~10의 int 변수를 3개 입력하세요", end = " ")
a, b, c = map(int, input().split())
print(a, b, c)
print(type(a), type(b), type(c))

if 5<a<10:
    print("5초과 10미만")
    if 7<a<9:
        print("7초과 9미만")
elif a<3:
    print("4")
else :
    print("0이상 3 이하")


for i in range(1,10):
    print(i) # 1~10-1(=9) 출력

for j in range(10,0,-1): # 10 ~ 0-(-1)(=1) 까지, offset이 -1인 수들 출력.
    print(j, end = " ")

z = 1

# while True를 사용해 10 이하의 홀수만 출력하는 코드 만들기.
while True :
    if z % 2 == 1 :
        print(z)
    z += 1
    if z > 10:
        break


# for문으로 구구단 만들기

for i in range(1,10) :
    for j in range(1,10):
        print(str(i)+"x"+str(j)+"=", i*j, end = " ")
    print("\n")
'''

# 별찍기 문제

# 왼쪽 정렬

for i in range(1,6):
    for j in range (1,i):
        print("*",end="")
    print("\n")

# 가운데 정렬

for i in range(1,6):
    for j in range(0,6-i):
        print("",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(0,6-i):
        print("",end=" ")
    print("\n")
