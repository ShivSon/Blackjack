def main():

# import all
	import random
	import sys

	print ("\n\nSo, you have decided to try your hand at Blackjack! Welcome to the table. \n\nThe rules of the game are simple. \nTry to get closer to 21 than me without going over. \nIf you go over the house wins. \nIf we tie, the house wins.\n\nGood Luck! \n\nI'll deal you in: \n")
# define player variables
	player_card_1 = random.randint(1,10)
	player_card_2 = random.randint(1,10)
	player_total = (player_card_1 + player_card_2)
# define dealer variables
	dealer_card_1 = random.randint(1,10)
	dealer_card_2 = random.randint(1,10)
	dealer_total = (dealer_card_1 + dealer_card_2)


	print (f"You have drawn a {player_card_1} and a {player_card_2}. Your total is {player_total}. \nMy face-up card is a {dealer_card_1}. \n")

	first_hit = input("Would you like to hit or stand? (press 'h' for hit or press any other key to stand?) \n")

	while True:

		while first_hit == "h":

# player has less than 21
			if (player_total) < 21:
				hit_me = random.randint(1,10)
				player_new_total = (player_total) + (hit_me)
				print(f"You have drawn a {hit_me}. Your new total is {player_new_total}")
				player_total = player_new_total
# player hits over 21 - loss
				if player_total > 21:
					print("You lose!")
					break
# player hits 21 exactly
				elif player_total == 21:
					print("21! You are close to the win...!")
					break
# continue hit loop
				user_input = input("\nWould you like to hit again or stand? (press 'h' for hit or press any other key to stand?) \n")
				if user_input == "h":
					continue

				else:
					break

		if player_total > 21:
			break
# dealer reveals hand
		print(f"\nMy face-down card was {dealer_card_2}. So my total is {dealer_total}")

# dealer hits if cards sum less than or equal to 16
		while (dealer_total) <= 16:
			hit_dealer = random.randint(1,10)
			dealer_new_total = (dealer_total) + (hit_dealer)
			print(f"I have drawn a {hit_dealer}. My new total is {dealer_new_total}")
			dealer_total = dealer_new_total
# dealer stands if cards sum are between 17 and 21
			if (dealer_total) >= 17 and dealer_total <= 21:
				print(f"I stand at {dealer_total}.")
				break
# dealer wins if player and dealer tie
			elif (dealer_total) == (player_total):
				print ("In the case of a tie, the house wins!")
				break
# dealer loses if card sums over 21
			elif (dealer_total) > 21:
				print("I have gone over 21, you win!")
				break
# exit loop if dealer over 21
		if (dealer_total) > 21:
			break
# exit loop if player total is higher than dealer total
		if (player_total) <= 21 and (player_total) > (dealer_total):
			print("You win!")
			break
# exit loop if dealer total is higher than player total
		elif dealer_total > player_total and dealer_total <= 21:
			print("I win! Better luck next time.")
			break
# exit loop if dealer and player tie
		else:
			dealer_total == player_total
			print("It's a tie, so I win! Better luck next time.")
			break

	cmd=input('Would you like to play again y/n? ')
# loop entire game
	if cmd=='y':
		main()
# exit game
	else:
		exit()
# start code
main()
