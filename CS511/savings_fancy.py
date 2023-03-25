print('Welcome to the savings calculator, what is your savings goal?')
saving_goal = float(input())
print('How much have you saved already?')
current_saving = float(input())

while True:
	print('How much are you saving every week?')
	weekly_save = float(input())
	if weekly_save != 0:
		break
	else:
		print("You need to save more than 0 dollars per week!")
		continue

# How many weeks it will take to save if less than 1 year (save time week)
stw = ((saving_goal - current_saving) / weekly_save)

# Integer value representing how many years it will take (save time year)
sty = ((saving_goal - current_saving) // weekly_save)

# Remainder of division for how many weeks after years have been removed (save time year remainder)
sty_remainder = ((saving_goal - current_saving) % weekly_save)

if current_saving >= saving_goal:
	print("You have already saved the intended amount!")
elif sty == 0:
	print('I have calculated that it will take ' + str(sty_remainder) + ' weeks to hit your savings goal!')
else:
	print('I have calculated that it will take ' + str(sty) + ' years and ' + str(sty_remainder) + ' weeks to hit your savings goal!')
