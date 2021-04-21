#chap4-1 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요."
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

#////////////////////////////////////

#chap4-2 슬라이싱
# jumin = "941217-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  # 0부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  #맨뒤에서 7번째부터 끝까지

#////////////////////////////////////

#chap4-3 문자열처리함수

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))#없으면 -1 출력
# #print(python.index("Java"))#없으면 오류로 다음 코딩 출력 불가
# print("hi")

# print(python.count("n"))

#////////////////////////////////////

#chap4-4 문자열포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." % 20) #d는 정수
# print("나는 %s을 좋아해요." % "파이썬") #s는 str
# print("Apple 은 %c로 시작해요" % "A") # c는 한글자
# # %s를 이용하면 다 수용가능
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "검은"))

# 방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요."  .format("파란", "검은"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "검은"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "검은"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "검은"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "검은", age = 20))

# 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#////////////////////////////////////

#chap4-5 탈출문자

# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# \' \" : 문장 내에서 따음표
# 저는 "곽희원"입니다.
# print("저는 '곽희원'입니다")
# print('저는 "곽희원"입니다')
# print("저는 \"곽희원\"입니다")
# print("저는 \'곽희원\'입니다")

# \\ : 문장 내에서 \
#print("C:\\Users\\hewo\\Desktop")

# \r : 커서를 맨 앞으로 이동
#print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")

# \t : 탭
#print("Red\tApple")

#////////////////////////////////////

#chap4-6 퀴즈 3

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 => nav + 5 + 1 + !

#내 코드
# site = "http://google.com"
# print(site)
# site1 = site[7:]
# print(site1)
# dot = site1.index(".")
# print(dot)
# site2 = site1[:dot]
# print(site2)
# pass1 = site2[:3]
# print(pass1)
# pass2 = len(site2)
# print(pass2)
# pass3 = site2.count("e")
# print(pass3)
# pass4 = "!"
# password = pass1 + str(pass2) + str(pass3) + pass4
# print(password)

#선생님 코드
# url = "http://naver.com"
# my_str = url.replace("http://","")#규칙1
# #print(my_str)
# my_str = my_str[:my_str.index(".")]#규칙2
# #print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))
