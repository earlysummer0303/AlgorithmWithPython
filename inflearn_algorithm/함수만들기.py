# def 키워드를 사용해서 함수 만들기

# 리턴값이 없는 함수.

def add(a,b): # 함수의 파라미터 명만 넣는다.
    c = a+b
    print(c)

add(1,3)

# 리턴값이 있는 함수.
def add2(a,b):
    c = a+b
    return c

print(add2(4,5))

# 파이썬에서는, 함수에서 두개 이상의 리턴값을 가질 수 있음.
# 이때, 리턴값 들은 튜플 자료형으로 리턴됨.

def calculate(a,b):
    c = a-b
    d = a+b
    return c, d

x = calculate(3, 2) #(1,5)
print(x)
print(x[0])









