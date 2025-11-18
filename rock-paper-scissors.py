from random import*

def ComputerDecision():
	if computerChoiceNo == 1:
		computerChoice = "rock"
	elif computerChoiceNo == 2:
		computerChoice = "paper"
	elif computerChoiceNo == 3:
		computerChoice = "scissors"
	else:
		print("Error 1")

	#print("Computer choice no: "+ str(computerChoiceNo))
	#print("computer choice "+ str(computerChoice))
	return computerChoice

def WinConditions(computerChoice):
	print(computerChoice)
	if computerChoice == "rock" and playerChoice == "paper":
		print("You win!")
	elif computerChoice == "paper" and  playerChoice == "scissors":
		print("You win!")
	elif computerChoice == "scissors" and  playerChoice == "rock":
		print("You win")
	elif computerChoice == playerChoice:
		print("Draw")
	else:
		print("You lose")

again = "y"
while again == "y":
	playerChoice = input("Rock, paper or scissors: ")
	computerChoiceNo = randint(1,3)
	computerChoice = None
	WinConditions(ComputerDecision())
	again = input("Again? (y/n): ")
