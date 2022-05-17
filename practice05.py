# 분기 - if문

weather = "비"
weather = input("오늘 날씨는 어때요? ") # input - 사용자가 임의로 값을 넣을 수 있다.
# if 조건 : 실행 명령문
if weather == "비" or weather == "눈": # or 로 조건문을 2개 넣을 수 있다.
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물은 필요 없어요.")


temp = int(input("기온은 어때요? ")) # input() 은 str 으로 받기 때문에 int() 로 감싸준다.

if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")
    
# 반복문 - for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


for waiting_no in [0,1,2,3,4,]:
    print("대기번호 : {}" .format(waiting_no))

for waiting_no in range(5): # 0 ~ 5 미만까지 주어진다.
    print("대기번호 : {}" .format(waiting_no))

for waiting_no in range(1, 5): # 1 ~ 5 미만까지
    print("대기번호 : {}" .format(waiting_no))
    

starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print("{}, 커피가 준비되었습니다." .format(customer))


# 반복문 - while
customer = "토르"
index = 5

while index >= 1:
    print("{}, 커피가 준비되었습니다. {}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{}, 커피가 준비되었습니다. 호출 : {}" .format(customer, index))
#     index += 1 # 무한루프...

customer = "토르"
person = "Unknown"

while person != customer:
    print("{}, 커피가 준비되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요? ")
    

# continue 와 break
absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와" .format(student))
        break
    print("{}, 책을 읽어봐" .format(student))
    

# 한 줄 for문
# 출석번화가 1, 2, 3, 4 앞에 100 을 붙이기로 -> 101, 102, 103, 104

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am Groot"]
print(students)
students = [i.upper() for i in students]
print(students)
students = [len(i) for i in students]
print(students)


'''
    Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
    50병의 승객과 매칭 기회가 있을 때, 총 탐승 승객 수를 구하는 프로그램을 작성하시오.
    
    조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
    조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
    
    (출력문 예제)
    [o] 1번째 손님 (소요시간 : 15분)
    [ ] 2번째 손님 (소요시간 : 50분)
    [o] 3번째 손님 (소여시간 : 5분)
    ...
    [ ] 50번째 손님 (소요시간 : 16분)
    
    총 탑승 승객 : 2 명
'''
from random import *
passangers_num = 1
possable_passangers = 0
while passangers_num <= 50:
    minute = int(random() * 46 + 5)
    if 5 <= minute <= 15:
        possable_passangers += 1
        print("[o] {}번째 손님 (소요시간 : {}분)" .format(passangers_num, minute))
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)" .format(passangers_num, minute))
    passangers_num += 1

print("총 탑승 승객 : {}" .format(possable_passangers))

# 강의풀이
cnt = 0 # 총 탑승 승객수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {}번째 손님 (소요시간 : {}분)" .format(i, time))
        cnt += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)" .format(passangers_num, minute))

print("총 탑승 승객 : {}" .format(cnt))
    