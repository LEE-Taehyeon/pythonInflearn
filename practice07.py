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
