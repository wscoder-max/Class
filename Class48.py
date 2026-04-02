import random

class FruitQuiz:
	def __init__(self):
		self.fruits = {'apple': 'red', 'orange': 'orange', 'watermelon': 'green', 'banana': 'yellow'}

	def quiz(self):
		while (True):
			fruit, color = random.choice(list(self.fruits.items()))
			
			print("What is the color of {}".format(fruit))
			user_answer = input()
			
			if(user_answer.lower() == color):
				print("Correct answer!")
			else:
				print("Wrong answer! The correct answer is {}".format(color))
				
			option = input("Would you like to play again? (y/n): ")
			if (option == 'y'):
				continue
			elif (option == 'n'):
				print("Thanks for playing!")
				break
			else:
				print("Invalid input. Please enter 'y' or 'n'.")

print("Welcome to the Fruit Quiz!")
quiz = FruitQuiz()
quiz.quiz()