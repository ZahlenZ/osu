import random
import time

print("Do you want to play a game? \nWelcome to Rock, Paper, Scissors!")
hand = 1
while True:
	hand = int(input("Please choose your implement! \n1 = Rock \n2 = Paper \n3 = Scissors \n0 = I don't want to play anymore or ever!\n"))
	if hand > 3:
		print("Please enter number in range [0:3].")
	elif hand == 0:
		print("Thanks for playing!")
		break
	else:
		challenge = random.randint(1, 3)
		print("The computer has rolled a : " + str(challenge) + " you rolled a : " + str(hand))
		if hand == 1 and challenge == 3:
			print("You Win!")
			time.sleep(1.75)
		elif hand == 3 and challenge == 1:
			print("You Lose!")
		elif hand < challenge:
			print("You Lose!")
			time.sleep(1.75)
		elif hand == challenge:
			print("It's a tie!")
		else:
			print("You Win! 🎉")
			time.sleep(1.75)
