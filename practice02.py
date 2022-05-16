# 연산자
print(1+1)
print(3-2)
print(5*10)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3) # 5 / 3 의 나머지 = 2
print(10%3) # 10 / 3 의 나머지 = 1
print(5//3) # 5 / 3 의 몫 = 1

print(10 > 3) # T
print(4 >= 7) # F
print(10 < 3) # F
print(5 <= 5) # T

print(3 == 3) # == 앞과 뒤의 값이 똑같은지 비교
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3) # 같지 않은지 비교
print(not(1 != 3)) # F

print((3 > 0) and (3 < 5)) # 두 항이 모두 T 여야 T
print((3 > 0) & (3 < 5)) # and 와 & 는 같은 의미

print((3 > 0) or (3 > 5)) # 두 항중 하나면 T 면 T 
print((3 > 0) | (3 > 5)) # or 과 | 는 같은 의미

print(5 > 4 > 3) # T
print(5 > 4 > 7)# F

# 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4
print(number) # 14
number = number + 2
print(number) # 16

number += 2 # number = number + 2 와 같은 의미
print(number) # 18

number *= 2
print(number) # 36
number /= 2
print(number) # 18
number -= 2
print(number) # 16

number %= 5
print(number) # 1

# 숫자처리함수
print(abs(-5)) # abs : 절대값
print(pow(4, 2)) # pow : 4^2 = 4*4 = 16
print(max(5, 12)) # max : 두 입력값 중 최대값 반환
print(min(5, 12)) # min : 두 입력값 중 최소값 반환
print(round(3.14)) # round : 반올림
print(round(5.92))

from math import * # math 라이브러리를 모두 이용하겠다.
print(floor(4.99)) # floor : 내림
print(ceil(3.14)) # ceil : 올림
print(sqrt(16)) # sqrt : 제곱근

# 랜덤함수
from random import *
print(random()) # random 함수를 통해 0.0 ~ 1.0미만의 임의의 값을 생성
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만
print(int(random() * 10) + 1) # 1 ~ 11 미만

print(int(random()) * 45 + 1) # 1 ~ 46 미만의 숫자 반환

print(randrange(1, 46)) # randrange : 뒤의 숫자는 포함 X. 1 ~ 46 미만의 숫자 반환

print(randint(1, 45)) # randint 는 양 끝의 숫자를 모두 포함


'''
    Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
    월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
    아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
    
    조건1 : 랜덤으로 날짜를 뽑아야 함.
    조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내롤 정함
    조건3 : 매원 1~3일은 스터디 준비를 해야하므로 제외
    
    (출력문 예제)
    오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) +"일로 선정되었습니다.")