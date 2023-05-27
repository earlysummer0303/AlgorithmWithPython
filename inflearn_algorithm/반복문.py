'''
반복문(for,while)
'''

# range 함수
a = range(10) # 순차적으로 해당 범위의(0부터 시작해서 파라미터값 개수의)int 값을 generate 하는 함수.
# range를 출력 할 때는 list형으로 형변환 해 출력해준다.
print(list(a)) # 배열 형태로 출력됨.

# for 반복문

# 반복문에서 range를 사용하는 형태가 swift와 비슷함
print("팩토리얼을 구할 수 입력")
b = input()
b = int(b)
c=1
for i in range(b):
    c *= i+1
print(b,"의 팩토리얼은",c)

# range를 다음처럼 시작하는 수와 요소의 개수로 표현할수도 있음
d = range(1,10) # 1부터 10-1(=9) 까지 표현

# 만약 역순으로 정렬된 배열을 출력하거나, 차이가 1이 아닌 int형의 배열을 출력하고 싶다면?
for j in range(10,0,-1): # 마지막에 offset 파라미터 추가.10부터 0-(-1)(=1) 까지 표현.
    print(j)


# while 반복문
i=1

while i<=10 :
    print(i)
    i+=1 #while문의 종료조건을 만족 시킬 수 있는 코드가 반드시 포함되어야 한다.

#무한 반복문 -> while True 키워드 사용

j=0
while True:
    print(j)
    j+=1
    if i%2 == 1:
        continue
    if j==10:
        break # break의 사용을 통해 반복문 빠져나오기.

#이중 for문

for i in range(1,6):
    for j in range(1,6):
        print(str(i)+"x"+str(j)+"=",i*j)
    print("\n")

#별찍기 문제

#왼쪽 정렬

for i in range(1,6):
    for j in range(0,i):
        print("*", end=" ")
    print("\n")

# 중앙 정렬

for i in range(1,6):
    for j in range(0,6-i):
        print("",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(0,6-i):
        print("",end=" ")
    print("\n")

# 오른쪽 정렬

for i in range(1,6):
    for j in range(0,6-i):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print("\n")

# 역순 왼쪽 정렬

for i in range(1,6):
    for j in range(5,0,-1):
        