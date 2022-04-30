import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((6, 7), dtype = 'int8')

def check_winner():
	for i in range(a.shape[0]):
		if np.all(a[i, 0:4] == 1) or np.all(a[i, 1:5] == 1) or np.all(a[i, 2:6] == 1) or np.all(a[i, 3:7] == 1):
			return 1
		if np.all(a[i, 0:4] == 2) or np.all(a[i, 1:5] == 2) or np.all(a[i, 2:6] == 2) or np.all(a[i, 3:7] == 2):
			return 2
	for i in range(a.shape[1]):
		if np.all(a[0:4, i] == 1) or np.all(a[1:5, i] == 1) or np.all(a[2:6, i] == 1):
			return 1
		if np.all(a[0:4, i] == 2) or np.all(a[1:5, i] == 2) or np.all(a[2:6, i] == 2):
			return 2
	for i in range(a.shape[0] - 3):
		for j in range(a.shape[1] - 3):
			if np.all([a[[i, i + 1, i + 2, i + 3], [j, j + 1, j + 2, j + 3]] == 1]):
				return 1
	for i in range(a.shape[0] - 3):
		for j in range(a.shape[1] - 3):
			if np.all([a[[i, i + 1, i + 2, i + 3], [j, j + 1, j + 2, j + 3]] == 2]):
				return 2
	for i in range(a.shape[0] - 3):
		for j in range(3, a.shape[1]):
			if np.all([a[[i, i + 1, i + 2, i + 3], [j, j - 1, j - 2, j - 3]] == 1]):
				return 1
	for i in range(a.shape[0] - 3):
		for j in range(3, a.shape[1]):
			if np.all([a[[i, i + 1, i + 2, i + 3], [j, j - 1, j - 2, j - 3]] == 2]):
				return 2
	return False

game_over = False
player_number = 1
while not game_over:
	print(a)
	#    plt.imshow(a, interpolation='nearest')
	#    plt.show()
	print("Player", player_number)
	while True:
		try:
			column = int(input("Which column do you wish to drop your piece? ")) - 1
			if 0 <= column <= 6:
				break
		except:
			pass
		print("Incorrect input, try again")
	for i in range(a.shape[0] - 1, -1, -1):
		if a[i, column] == 0:
			a[i, column] = player_number
			break
	if player_number == 1:
		player_number = 2
	else:
		player_number = 1
	game_over = check_winner()
print(a)
# plt.show()
print("Congrats! Player " + str(game_over) + " wins!")
