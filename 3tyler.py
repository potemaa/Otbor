def is_prime(x):#функция проверки простоты числа
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True
for x in range(1,4):#перебираем возможные цифры в записи операнд
	for y in range(1,4):
		res=x+6*7+x*(7**2)+y*(7**3)+y*(7**4)+2*(7**5)+y+(x*5)+y*(5**2)+3*(5**3)+2*(5**4)+3*(5**5)
		if is_prime(res):
			sc=sum([int(a) for a in str(res)])#сумма цифр
			if sc%13 ==0:
				print(sc,res)
