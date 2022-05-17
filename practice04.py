# 리스트

# 지하철 칸 별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 다음 정류장에서 하하씨가 탔을 때,
subway.append("하하")
print(subway)

# 정형돈씨가 유재석과 조세호 사이에 탈 때,
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 뒤에서 한명씩 꺼냄
print(subway.pop())
print(subway)

# 같은 이름이 있는 사람이 몇명인지 확인하기
print(subway.count("유재석"))

# 리스트 정렬
num_list = [5, 3, 1, 2, 4]
num_list.sort()
print(num_list)

# 리스트 뒤집기
num_list.reverse()
print(num_list)

# 리스트 값 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [12, 6, 8, 98, 54]
num_list.extend(mix_list)
print(num_list)

# 사전 - key:value / key는 중복이 허용되지 않는다.
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 해당 key 값이 없으면 "None" 리턴

# print(cabinet[5]) # 해당 key 값이 없으면 오류발생


print(cabinet.get(5)) # 해당 key 값이 없으면 "None" 리턴
print(cabinet.get(5, "사용불가->사용가능")) # key값이 5인 값을 리턴, 없으면 "사용불가->사용가능" 을 리턴

print(3 in cabinet) # key 갑이 3인 값이 cabinet에 있는가? 있으면 T / 없으면 F 리턴

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새로운 값 삽입
cabinet["C-20"] = "조세호" # 만일 key 값이 C-20 인 값이 있으면 덮어씌운다.
print(cabinet)

# 원하는 값 삭제
del cabinet["A-3"]
print(cabinet)

# key / value 각각의 값만 출력
print(cabinet.keys())
print(cabinet.values())

# key-value 값 출력
print(cabinet.items())

# 사전 모두 삭제
cabinet.clear()
print(cabinet)

# 튜플 - 내용변경, 추가는 안됨. 단, 속도가 리스트보다 빠르다.
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# manu.add("생선가스") # 튜플은 내용변경이 안됨 - 에러

name = "김종국"
age = 20
hobby = "코딩"

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# set : 중복이 안되고, 순서가 없는 자료구조
my_set = {1,2,3,3,4}

print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# java 와 python 모두를 할 수 있는 사람(교집합)
print(java & python)
print(java.intersection(python))

# 둘 중 어느 하나를 할 수 있는 사람(합집합)
print(java | python)
print(java.union(python))

# 차집합(java는 가능, python은 불가능)
print(java - python)
print(java.difference(python))

# python 집합에 add
python.add("김태호")
print(python)

# java set 에서 김태호를 뺌.
java.remove("김태호")
# java.remove("김태호") # 없는 값을 없애려고 한다면 에러발생.
print(java)

# 자료구조 서로 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# set 을 list 로 변경
menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


'''
    Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
    참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
    추첨 프로그램을 작성하시오.
    
    조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20으로 가정
    조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
    조건3 : random 모듈의 suffle 과 sample 을 활용
    
    (출력 예제)
    -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자 : [2, 3, 4]
    -- 축하합니다. --
    
    (활용 예제)
    from random import *
    lst = [1, 2, 3, 4, 5]
    print(lst)
    shuffle(lst)
    print(lst)
    print(sample(lst, 1))
'''

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

print("----------------")
students = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# users = range(1, 21) but type 이  range 다. -> list(users) 로 해야 list 로 저장.
# select = sample(students, 4) -> 한번에 4명을 뽑는 방법.
shuffle(students)
first = sample(students, 1)
students.remove(first[0])
secondToFourth = sample(students, 3)


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}" .format(first))
print("커피 당첨자 : {}" .format(secondToFourth))
print("-- 축하합니다. --")