# chap11-1 모듈
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# #price_soldier(5) # 안됨

# from theater_module import price_soldier as price
# price(5)

# chap11-2 패키지
# import travel.thailand
# #import travel.thailand.ThailandPackage#하면 안됨 class로 끝나면 안 돌아가짐
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #from random import *
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# # travel에 있는 __init__에 따라 구동됨

# # chap11-5 패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# chap11-6 pip install
# 구글에 "pypi"입력 후에 사이트 들어가고 원하는 패키지 다운 받으면 됨
# 원하는 패키지를 찾으면 터미널에 붙여넣기해서 다운 받으면 됨
# 터미널에 "pip list" 치면 다운 받은 패키지 목록 나옴
# 터미널에 "pip show (패키지 이름)" 패키지 정보 보여줌
# 터미널에 "pip install --upgrade (패키지 이름)" 버전 업그래이드함
# 터미널에 "pip uninstall (패키지 이름)" 패키지 삭제


# chap11-7 내장 함수
# input : 사용자 입력을 받는 함수

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 구글에 "list of python builtins"로 검색하면 "Built-in Functions"에 내장 함수 설명 있음, 한국어 있음

# chap11-8 외장 함수

# 구글에 "list of python modules"로 검색하면 "Python Module index"에 외장 함수 설명 있음 예재도 있음

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후

# Quiz) 프로잭트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유투브 : http://youtube.com
# 이메일 : nadocoding@gmail.com

#선생님 코드 == 내 코드