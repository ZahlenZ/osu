print('Welcome to the savings calculator, what is your savings goal?')
saving_goal = float(input())
print('How much have you saved already?')
current_saving = float(input())
print('How much are you saving every week?')
weekly_save = float(input())

weeks_togoal = ((saving_goal - current_saving) / weekly_save)

print('I have calculated that it will take ' + str(round(weeks_togoal)) + ' weeks to hit your savings goal!')
