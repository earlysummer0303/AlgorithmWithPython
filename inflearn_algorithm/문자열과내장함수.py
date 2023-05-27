'''
내장함수란? : 특정 package를 import 하지 않아도, python 언어 내부적으로 구현되어있는 함수 / 메소드
'''

# str 타입의 내장함수들

# 1. 문자열의 모든 영문을 upper case / lower case 로 변환해주는 내장함수 => upper() / lower()

a = "Hi My Name Is Swimmer"
print(a.upper())
print(a.lower())

# 2. 문자열에서 특정 char의 첫 번째 인덱스를 반환하는 내장함수 => find(chr)

print(a.find("M")) #3

# 3. 문자열에서 특정 char의 개수를 반환하는 내장함수 => count(chr)

print(a.count("m")) #3

# 4. 문자열 슬라이스 => 서브스크립션 이용

b = "abcd efg"
print(b[:2]) # ab, index 2 가 slice의 border, index 0 ~ 2미만 까지의 요소만을 반환.
print(b[3:5]) # d , index 5 가 slice의 border, index 3 ~ 5미만 까지의 요소만을 반환.

# 5. 문자열의 길이 구하기 => len(str)
print(len(b))

# 문자열은 배열의 성질을 가진다.

for i in range(len(b)):
    print(b[i],end="") #abcd efg 그대로 출력.
print()
for i in b:
    print(i, end = "") # 이렇게 배열의 item으로도 표현 가능 (배열의 각 item은 char 형)

# 대(소)문자인지 판별하는 함수 => isupper() / islower()
print()
c = "Jiwoo Is Swimmer"
for i in c:
    if i.isupper(): # upper case일 경우 true return
        print(i, end=" ")

# 알파벳인지(= 공백이 아닌 문자인지) 판별하는 함수 => isalpha()
print()
d = "IT IS TRUE"
for i in d:
    if i.isalpha():
        print(i, end="")

# 해당 문자의 아스키 넘버를 출력하는 함수 => ord(chr)
print()
e = "QW"
for i in e:
    print(ord(i)) # 81, 87

# 특정 아스키넘버의 char을 알려면?

print(chr(65))