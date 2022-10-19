
b=4
c=3
print(b/c) #파이썬에서는 이게 몫을 의미하는게 아니라 나누어진 값을 의미.
print(b//c) #이게 몫입니다.
#제곱 하기
print(4**2) #4의 제곱
print(4**3)

# 문자열 알아보기
    # 따옴표나 큰따옴표로 표현 가능
stringring = 'jiwoo\'s boko' 
# 작은 따옴표로 했을때, 문장 중간에 들어가는따옴표 전에는 백슬래쉬
# 점투파 '이스케이프 코드' 참고
# 같은 문자열을 여러번 출력하기
a = "가나다라"
print(a*4)

# 문자열 인덱싱
print(stringring[0]) # 문자열 가장 앞 문자 (s)
print(stringring[-1]) # 문자열 가장 뒤 문자 (k)
#문자열 슬라이싱
print(stringring[0:10:1]) # 대괄호 안의 숫자는 각각 이상, 미만, 간격
# 위처럼, 인덱스 0~10까지 한칸 간격으로 출력된다.

#문자열에 변수 넣기
a = "three"
b = 3
 
c = "I ate %s apples so I was sick for %d days" % (a,b)
print(c)

# 변수 포맷팅 하기
a = "가나다라 {황지우} 마바사 ".format(황지우 = "jade")
print(a)

# 리스트
a = ["황지우","김서하","임채승","최명선"]

# 리스트의 내용물을 교체해보자
a[0:2] = ["해리","로로"]
print(a)