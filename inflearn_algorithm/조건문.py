'''
조건문 if (분기, 중첩)

'''

# if 문
x = 7
if x==7 :
    print("Lucky")
# 파이썬의 조건문은 스코프 {} 를 사용하지 않으며, 콜론을 찍고 조건문의 내용을 들여쓰기로 표현해준다.
# 이때, 내부 코드는 한줄씩, 무조건 'tab키 한 칸' 들여쓰기 해줘야 한다. (안그러면 에러...)

# 중첩 if 문 
y = 15

if y >= 10 :
    print("10 이상")
    if y == 15 :
        print("15이다.")

# 여러개의 조건을 가지는 if 문

z=9

if z>7 and z<10 : # 여러개의 조건을 열거할때 &&이 아니라 and 키워드를 써준다.
    print("8이나 9 올시다.")

if 6<z<12 :
    print("아니 이게 된다고?") # 조건을 여러개 열거할 뿐 아니라, 한 문장의 부등호 관계로도 표현도 가능하다.

# 분기문 (if-else)

if z<7 :
    print("7보다 작은 수")
else :
    print("7 이상의 수")

# else if 의 경우, elif 키워드를 사용.

if z<7 :
    print("7보다 작은 수")
elif z == 7 :
    print("7이다.")
else :
    print("7보다 큰 수")
