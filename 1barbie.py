a = int('24102205', 7)  # первое слагаемое
b = int('16056872', 9)  # второе слагаемое
c = a + b  # результат выражения
print(c)
for base in range(2, 20):  # перебор систем счисления
	x = c
	otv = ''
	while x > 0:
		otv = str(x % base) + otv
		x //= base
	if '2023' in otv:
		print(otv, base)
