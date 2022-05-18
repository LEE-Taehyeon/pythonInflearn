# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")
    
open_account()


def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면 출금 가능
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다." .format(balance))
        return balance

def withdraw_night(balance, money): # 밤에 출금, 수수료 부과
    commission = 100
    return commission, balance - money - commission # 여러개(튜플)의 값을 리턴할 수 있다.


balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다." .format(commission, balance))


# 함수의 기본값 설정

def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 사용언어 : {2}" \
        .format(name, age, main_lang)) # \ : 줄바꿈(나눠진 두 문장은 한문장으로 인식된다.)

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 같은 학교, 같은 학년, 같은 반, 같은 수업 을 듣는 학생 -> 기본값 설정
def profile(name, age=17, main_lang = "파이썬"): # 파라미터 값을 전달 받지 않으면 기본값으로 설정
    print("이름 : {0}\t 나이 : {1}\t 사용언어 : {2}" \
        .format(name, age, main_lang)) # \ : 줄바꿈(나눠진 두 문장은 한문장으로 인식된다.)

profile("유재석")
profile("김태호")


# 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(age = 17,name = "김태호", main_lang = "파이썬")


# 가변인자를 활용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end =" ")
    # end = "" : 기본적으로 print 문은 한문장 끝나면 줄바꿈을 하는데,
    # end = " " 를 넣으면 평소대로 줄바꿈을 하지 않고 " " 로 문장을 마무리 하겠다는 뜻.
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 이때, lang를 하나 늘려서 호출하고 싶으면 함수 자체를 변경해야한다.
# 이때, 사용할 수 있는게 "가변인자" 이다.
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end =" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 27, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 21, "Kotlin", "Swift")


# 지역변수와 전역변수
# 지역변수 : 함수 내에서만 사용할 수 있는 함수.
# 전역변수 : 모든 공간에서 사용할 수 있는 함수.

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용. 일반적으로 전역변수를 권장하지는 않음.
    # 따라서 함수의 파라미터로 받아서 사용하는 것을 권장.
    gun = gun - soldiers # 지역변수 - 위의 gun 과는 다른 gun 이다.
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))


'''
    Quiz) 표중 체중을 구하는 프로그램을 작성하시오.
    # 표준 체중 : 각 개인의 키에 적당한 체중
    
    (성별에 따른 공식)
    남자 : 키(m) x 키(m) x 22
    여자 : 키(m) x 키(m) x 21
    
    조건1 : 표준 체중은 별도의 함수 내에서 계산
            # 함수명 : std_weight
            # 전달값 : 키(height), 성별(gender)
    조건2 : 표준 체중은 소수점 둘째자리까지 표시
    
    (출력 예제)
    키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender): # 키는 m 단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # round 함수 : round(%%%, 3) - 소수점 3번째 자리에서 반올림해줘.
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))