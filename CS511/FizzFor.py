n = input('Please enter a number: ')
for n in range(1, int(n) + 1):
	if n % 3 == 0 and n % 5 == 0:
		print(str(n) + ' Fizz Buzz')
	elif n % 3 == 0:
		print(str(n) + ' Fizz')
	elif n % 5 == 0:
		print(str(n) + ' Buzz')
	else:
		print(n)
print('Done!')

print('I have made some changes.')