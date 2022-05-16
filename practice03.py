# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990123-1234567"
print("성별 : "+ jumin[7])
print("연 : " + jumin[0:2]) # 0:2 = 0번째 부터 2번째 직전(index 1번)까지 값 출력
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 0번째부터 가져오려면 0 생략해도 된다.
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 마지막까지 가져오려면 마지막 숫자 생략해도 된다.
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤는 -1부터 시작

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자
print(python.upper()) # 모든 문자 대문자
print(python.isupper) # 맨 앞자리가 대문자인디
print(len(python)) # 문자열 길이
print(python.replace("Python", "Jave"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 앞의 index 에 +1 한 위치부터 찾아봐라
print(index)

print(python.find("n"))
print(python.find("Java")) # 내가 찾는 문자가 없으면 -1 반환
# print(python.index("Java")) # 내가 찾는 문자가 없으면 error 반환. 이 뒤는 진행안됨.
print(python.count("n")) # n 이 몇번나오는지 반환

# 문자열 포맷
print("a" + "b")
print("a", "b") # ,는 띄어쓰기 한칸이 추가

print("나는 %d살입니다." % 20) # 정수 - %d
print("나는 %s을 좋아해요" % "파이썬") # 문자열 - %s
print("Apple 은 %c로 시작해요" % "A") # 한글자 - %c

print("나는 %s살입니다." % 20) # %s - 모두 다 가능

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

age = 28
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")
# 저는 "나도코딩" 입니다. 라고 출력을 원함
print("저는 '나도코딩' 입니다.") # 작은따옴표로 나옴
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.") # \" 는 그대로 " 를 출력
print("저는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서는 \ 하나로 인식
print("C:\\Python\\PythonWorkspaces\\pythonInflearn> ")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # Red Apple 까지 작성하고 커서를 맨앞으로 다시 이동해서 Pine 을 쓴다. 즉 결과값은 PineApple 로 반환

# \b : 백스페이스(한글자 삭제)
print("Redd\bApple") # RedApple 반환

# \t : tab 역할
print("Red\tApple")


'''
    Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
    예) http://naver.com
    규칙1 : http:// 부분은 제외 => naver.com
    규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com
    규칙3 :  남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
    
    예) 생성된 비밀번호 : nav51!
'''

url = "http://naver.com"
princple1 = url[7:]
princple2 = princple1[:princple1.find(".")]
princple3 = princple2[:3] + str(len(princple2)) + str(url.count("e")) + "!"

print("생성된 비밀번호 : %s" % princple3)

my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("생성된 비밀번호 : {}" .format(password))