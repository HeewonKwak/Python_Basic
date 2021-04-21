# chap10-1 예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2])
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# chap10-2 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}"..format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# chap10-3,4 사용자 정의 에러, finally
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}"..format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("알 수 없는 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally: # 어떤 에러가 생겨도 수행해서 강제 종료되는 위험이 없게함
#     print("계산기를 이용해 주셔서 감사합니다.")

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken: #남은 치킨보다 주문량이 많을때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#             ,format(waiting, order))
#         waiting += 1
#         chicken -= order
# [내 코드] # 틀린거 2개 있음 보고 찾으라
# class SoldOutError(Exception):
#     pass

# try:
#     chicken = 10
#     waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
#     while(True):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        
#         if order < 1 or type(order) != int:
#             raise ValueError
        
#         if order > chicken: #남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#             if chicken == 0:
#                 raise SoldOutError
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError:
#     print("재고가 소진되어 더 이상 주문을 받지 않습니다.")


# [선생님 코드]
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
            
        if order > chicken: #남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break