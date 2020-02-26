# class responsible to print the board and the win/lose message
class Hangman(object):

	def __init__(self, chances=6):
		self.chances = chances

	def get_man(self, miss):

		if miss == 0:
			print('''
					+---+
					|   |
						|
						|
						|
						|
					========= ''')
		elif miss == 1:
			print('''
					+---+
					|   |
					O	|
						|
						|
						|
					=========''')
		elif miss == 2:
			print('''
					+---+
					|   |
					O   |
					|   |
						|
						|
					=========''')
		elif miss == 3:
			print('''
					 +---+
					 |   |
					 O   |
					/|   |
						 |
						 |
					=========''')
		elif miss == 4:
			print('''
					 +---+
					 |   |
					 O   |
					/|\  |
						 |
						 |
					=========''')
		elif miss == 5:
			print('''
					 +---+
					 |   |
					 O   |
					/|\  |
					/    |
						 |
					=========''')
		elif miss == 6:
			print('''
					 +---+
					 |   |
					 O   |
					/|\  |
					/ \  |
						 |
					=========''')
		else:
			print("0")

	def get_win(self):
		return print("\nEnd game, you win!")

	def get_game_over(self):
		return print("\nEnd game, you lose!")

