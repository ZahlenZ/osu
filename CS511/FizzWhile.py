n = int(input('Please enter a number: '))
count = 1
while count <= n:
	if  count % 3 == 0 and count % 5 == 0:
		print(str(count) + ' Fizz Buzz')
	elif count % 3 == 0:
		print(str(count) + ' Fizz')
	elif count % 5 == 0:
		print(str(count) + ' Buzz')
	else:
		print(count)
	count = count + 1
print('Done!')