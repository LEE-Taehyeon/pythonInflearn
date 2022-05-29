# 표준 입출력

print("Python", "Java", sep = ",") # sep(seperate) : 각 문장을  sep 에서 선언한 것으로 구분.
print("Python", "Java", sep = ",", end = "?") # end : 문장의 끝부분을 ""에 들어있는 문자로 바꿔주세요 라는 뜻.
print("무엇이 더 재밌을까요?") # 따라서 두개의 print 문장이지만 한줄로 출력된다.

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)
# stdout : 표준출력으로 문자출력
# stderr : 표준에러로 처리


scores = {"수학":0, "영어":50, "코딩":100} # dictionary
for subject, score in scores.items(): # items : key-value 쌍의 튜플로 전송
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust(%) : 왼쪽으로 정렬을 하는데 총 %칸의 공간을 확보해서 정렬해라.


# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(%) : % 만큼의 공간을 확보하고 숫자를 넣는데 남은 수는 0으로 채운다.
    
    
# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # input : 사용자가 임의의 값을 넣어주어야함.
# input 으로 받은 값의 타입은 str(문자열).
print("입력하신 값은 " +  answer + "입니다.")


# 다양한 출력 포맷
# 1. 빈자리는 빈공간으로 두고, 오른쪽으로 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}" .format(500))

# 2. 양수일때는 + 로 표시, 음수일때는 -로 표시
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500))

# 3. 왼쪽 정렬, 빈칸은 _ 로 채움
print("{0:_<10}" .format(500))

# 4. 3자리마다 콤마(,) 찍기
print("{0:,}" .format(10000000000000))

# 5. 3자리마다 콤마(,) 찍기
print("{0:,}" .format(10000000000000))

# 6. 3자리마다 콤마(,) 찍기, 부호 추가
print("{0:+,}" .format(10000000000000))
print("{0:+,}" .format(-10000000000000))

# 7. 3자리마다 콤마(,) 찍기, 부호 붙이기, 자릿수 확보, 빈자리 ^ 채우기
print("{0:^<+30,}" .format(1000000000000000)) # 30 자리만큼의 공간 확보

# 8. 소수점 출력
print("{0:f}" .format(5/3))

# 8. 특정 자리수까지의 소수점 출력
print("{0:.2f}" .format(5/3)) # .2 : 소수점 2번째자리까지만 출력(소수점 3번째 자리에서 반올림)


# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # 처음 "" : 파일이름, 두번째 "W" : 쓰기위한 목적, encoding="utf8" : utf8 을 해주지 않으면 한글을 가져올 때 깨질 수 있다.
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일을 열면 무조건 닫아주어야 한다.
# 1. open 으로 score.txt 파일을 쓰기 목적으로 열고
# 2. print 문을 파일에 쓰고 (score.txt 파일이 생성)
# 3. 파일을 닫는다.

score_file = open("score.txt", "a", encoding="utf8") # 내용을 덮어쓰는게 아니라 이어서 쓰고 싶으면 "a"
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # print 문으로 작성하면 자동 줄바꿈이 되는데 write 로 하면 줄바꿈 안됨.
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # "r" : read
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # "r" : read
print(score_file.readline(), end="") # 한줄씩 읽어오고, 커서는 다음줄로 이동
print(score_file.readline()) 
print(score_file.readline()) 
# print(score_file.readline()) 

# 출력해야 하는 파일의 줄 수를 모를때.
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 가져와서 list 형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()


# pickly : 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장하는 것
#           갖고 있는 데이터를 pickle 을 이용하여 어떤 파일에 저장하고, 해당 내용을 load 를 통해 불러와서 변수에 저장해서 사용할 수 있게 해주는 라이브러리.
import pickle
profile_file = open("profile.pickle", "wb") # pickly 을 사용하기 위해선 b(binary) 를 설정해주어야 하고, encoding 은 따로 안해도 된다.
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)

# pickly 을 이용해서 이 데이터를 파일에 써야한다.
pickle.dump(profile, profile_file) # profile 에 있는 정보를 파일에 저장.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile_= pickle.load(profile_file) # 파일에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()


# with
import pickle

with open("profile.pickle", "rb") as profile_file:  # 이 파일 정보를 profile_file 라는 변수에 저장
    print(pickle.load(profile_file))
# 따로 close 문이 없어도 된다.

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
    
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
    

'''
    Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
    보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
    
    - x 주차 주간보고 -
    부서 :
    이름 : 
    업무 요약 : 
    1 ~ 50 주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
    
    조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

for number in range(1,11): # 50 주차는 너무 많으니 10 주차까지
    with open(f"{number}주차.txt", "w", encoding="utf8") as week_reports: # 이 파일 정보를 week_reports 라는 변수에 저장
        week_reports.write(f" {number} 주차 주간보고 -")
        week_reports.write("\n부서 : ")
        week_reports.write("\n이름 : ")
        week_reports.write("\n업무 요약 : ")


