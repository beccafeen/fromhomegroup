def odds_and_evens():

	import random
	print("Let's play Odds and Evens!\nYou have $50.")
	money=50

	while money>=5:
		wager = int(input("Will you wager $[5] or $[10]?"))
		numbs = input("Will you play for [odds] or [evens]?")
		finger = int(input("Will you point with [1] or [2] fingers?"))
		print("You pointed with", finger,"fingers.")
		finger_comp = random.randint(1,2)
		print("I pointed with", finger_comp,"fingers")
		bet = finger+finger_comp

		if (numbs=="odds"):
			if (bet==3):
				money=money+wager
				print("The result is odd")
				print("You win! You now have $",money)
			elif (bet==2 or 4):
				money=money-wager
				print("The result is even")
				print("You lose! You now have $",money)
		elif (numbs=="evens"):
			if (bet==3):
				money=money-wager
				print("The result is odd")
				print("You lose! You now have $",money)
			elif (bet==2 or 4):
				money=money+wager
				print("The result is even")
				print("You win! You now have $",money)

		answer = input("Play again? Y/N\n")
		if (answer not in ("Y","y") or money<5):
			return
#odds_and_evens()
