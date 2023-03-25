import sys
import re

file = open(sys.argv[1])
madlib = file.read()
file.close()
regex = re.compile('\[.+?\]')

while True:
	match = regex.search(madlib)
	if not match:
		break
	elif match.group()[1] == 'a':
		print('Please provide an ' + str(match.group()[1:-1]) + ':')
	else:
		print('Please prove a ' + str(match.group()[1:-1]) + ':')
	word = input()
	madlib = madlib.replace(match.group(), word, 1)

out = open(sys.argv[2], 'w')
out.write(madlib)
out.close()

