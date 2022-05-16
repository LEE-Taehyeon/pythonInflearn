# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9) # 문자열과 숫자의 연산 가능

# boolean 자료형(참/거짓)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요~
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
name = "똘똘이" # 변수를 중간에 설정하면 이 후 코드는 바뀐 값으로 변경된다.
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 정수형을 + + 를 포함한 문자열에 사용하기 위해서는 str 함수를 사용하여 감싸주어야 한다.
print(name + "는 어른일까요? " + str(is_adult))
# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9) # 문자열과 숫자의 연산 가능

# boolean 자료형(참/거짓)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요~
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
name = "똘똘이" # 변수를 중간에 설정하면 이 후 코드는 바뀐 값으로 변경된다.
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 정수형을 + + 를 포함한 문자열에 사용하기 위해서는 str 함수를 사용하여 감싸주어야 한다.
print(name, "는 ",age, "살이며, ",hobby, "을 아주 좋아해요") # , 를 이용하여 문장을 합칠 수도 있다. 이때는 정수형, boolean 변수를 그대로 사용 가능하다. 단 ,를 사용하면 띄어쓰기 한칸이 들어가게된다.
print(name + "는 어른일까요? " + str(is_adult))

# 주석
# 한문장 주석은 : #
'''
    여러문장을 주석하고 싶으면  ' 세개를 쓰면 된다.
    주석을 편하게 하고 싶으면 여러문장을 drag 하고 ctr + / 하면 된다.
'''

'''
    Quiz) 변수를 이용하여 다음 문장을 출력하시오.
    
    변수명 : station
    변수값 :  "사당", "신도림", "인천공항" 순서대로 입력
    출력문장 : XX 행 열차가 들어오고 있습니다.
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인청공항"
print(station + "행 열차가 들어오고 있습니다.")