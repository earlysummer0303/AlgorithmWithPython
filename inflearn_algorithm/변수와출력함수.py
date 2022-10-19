# 1. 변수와 출력함수 

'''
    변수명 정하기)
    - 영문, 숫자, 언더바로 이루어짐
    - Case Sensitive
    - 문자 혹은 _ 로 시작 가능
    - 숫자, 특수문자로 시작할 수 없으며, 파이썬 키워드 사용 불가.

'''

# 변수 선언시 타입을 명시하지 않는다.

a = 2+3
b = 7
c = 8
print(a) # 파이썬의 프린트 함수는 terminator 가 "\n" 이다.
print(a,b,c) # 파이썬의 프린트 함수는 아이템간 seperator 가 " " 이다. 

d,e,f = 1,2,3 # 이처럼 변수명을 , 로 열거하고, 그 값을 열거하는 식으로 할당할 수 있다.
print(d,e,f)

# 값 교환
a,b = 10,20
# 값 교환시, 다른 언어 처럼 temp 값을 사용해주지 않아도 된다.
a,b = b,a
print(a,b)

# 변수 타입
a = 12345
print(type(a)) # int
a = 12.12
print(type(a)) # float
a = 'student' # 문자열 사용할때 작은따옴표('') 사용. -> 쌍따옴표도 가능
b = 'a'
print(type(a),type(b)) # a,b 둘다 str 타입

# 프린트 함수의 seperator 적용
print(a,b,sep=',')

# 프린트 함수의 terminator 적용
print(a,end='  ')
print(b,end='  ')