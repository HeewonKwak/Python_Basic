#chap5-1 리스트

#리스트 []

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

#순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# chap5-2 사전

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# print(cabinet[5])#값이 없을시 오류를 출력
# print(cabinet.get(5))#값이 없을시에 none을 출력
# print(cabinet.get(5, "사용가능")) # none 대신에 다른 값 출력 가능

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# 간 손님
#del cabinet["A-3"]
#print(cabinet)

# key 들만 출력
#print(cabinet.keys())

# value 들만 출력
#print(cabinet.values())

# key, value 쌍으로 출력
#print(cabinet.items())

# 목용탕 폐점
# cabinet.clear()
# print(cabinet)

# chap 5-3 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add 안됨

# (name, age, hobby) = ("김종국", "20", "코딩")
# print(name, age, hobby)

# chap 5-4 세트

# 집합 (set)
# 중복 안됨, 순서 없음
#my_set = {1,2,3,3,3}
#print(my_set)

#java = {"유재석", "김태호", "양세형"}
#python = set(["유재석", "박명수"])

# 교집합
#print(java & python)
#prin(java.intersection(python))

# 합집합
#print(java | python)
#print(java.union(python))

#차집합
#print(java - python)
#print(java.difference(python))

# 추가
#python.add("김태호")
#print(python)

# 제거
#java.remove("김태호")#print(java)

# chap5-5 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#퀴즈4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였도 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 솽관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# 1st = [1,2,3,4,5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st,1))

# 내 코드
# from random import *
# st = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(st)
# sample(st,4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}\n커피 당첨자 : {1}".format(st[0],st[1:4]))
# print("-- 축하합니다 --")

#선생님 코드
# from random import *
# users = range(1,21)
# print(type(users))
# users = list(users)
# print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")