#과제 : 1부터 10까지 반복하는 과정에서 3의 배수일 걍우, year를 출력하시오.
#5의 배수일때 dream출력
# 15의 배수일 때 yeardream 출력
#나머지  모든 경우는 숫자 그대로 출력
print('hello')

for i in range(1,21) :
	if i%15 == 0 :
		print("yeardream")
	elif i%3 == 0 :
		print("year")
	elif i%5 == 0 :
		print("dream")
	else :
		print(i)


