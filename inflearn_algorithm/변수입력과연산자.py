#2. 변수 입력과 연산자


# 파이썬에서는 input() 함수를사용해서 input을 받는다.

'''
print("숫자를 입력하세요 : ",end=" ")
e = input()
print("결과값은 : ",e)
'''

# 여러개의 input을 한번에 받는 방법 -> 변수를 처음부터 여러개 할당한 후 input함수로 받고 split

'''
a, b = input("숫자를 입력하세요 : ").split()
#split() 함수는 기본적으로 스페이스 한 칸을 seperator 로 인식한다. (sep 파라미터의 기본값이 " ")
print(a,b)
#input()함수는 기본적으로 str형으로 반환한다.
print(type(a)) # <class 'str'> -> 파이썬은 클래스를 카멜케이스로 쓰는구나
c = int(a)+int(b)
print("int 형변환 해서 합하면 ->",c)

'''
# 처음부터 형변환 해서 받아버리려면? -> map 함수 사용 -> map(형변환할 타입, 형변환할 내용)

a,b,c = map(int,input().split())
print(a+b+c)

