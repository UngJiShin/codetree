year=int(input())
# if year % 4 == 0:
#     # 조건1이 참일 때 실행하는 코드
#     print("true")
#     if year % 100 == 0:
#         # 조건1과 조건2가 모두 참일 때 실행하는 코드
#         print("true")    
#     else:
#         # 조건1은 참이지만 조건2는 거짓일 때 실행하는 코드
#         print("false")
# else:
#     print("false")
#     # 조건1이 거짓일 때 실행하는 코드
if year % 4 == 0:                                  
	if year % 400 == 0:                            
		print("true")
	elif year % 100 == 0:                          
		print("false")
	else:
		print("true")                         
else:
	print("false")