def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True
a = 228**2024+52**522+14**4+1
base = 51
new = ''
while a > 0:
	remain = a % base
	new = str(remain) + new
	a //= base

for a in '0123456789':
	if is_prime(new.count(a)):
		print(a)