import pygame
import ctypes
import numpy as np

pygame.init()
user32 = ctypes.windll.user32
screen = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), pygame.FULLSCREEN)
myfont = pygame.font.SysFont('Comic Sans MS', 40)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption('Connect 4')

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

def drawBoard():
	global player_number
	screen.fill((25, 155, 155))
	for i in range(1, 9):
		pygame.draw.line(screen, (0, 0, 0), (i * w / 9, 35 + h / 8), (i * w / 9, 25 + 7 * h / 8), 10)
	for i in range(1, 8):
		pygame.draw.line(screen, (0, 0, 0), (w / 9 - 4, 30 + i * h / 8), (8 * w / 9 + 5, 30 + i * h / 8), 10)

def getColumn():
	global player_number
	pygame.draw.rect(screen, (25, 155, 155), pygame.Rect(0, 0, 330, 100))
	textsurface = myfont.render('Player ' + str(player_number) + '\'s turn:', False, (0, 0, 0))
	screen.blit(textsurface, (30, 30))
	textsurface0 = myfont.render('Which column do you wish to drop your piece?', False, (0, 0, 0))
	screen.blit(textsurface0, (330, 30))
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_1:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 0] == 0:
					a[i, 0] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_2:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 1] == 0:
					a[i, 1] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(2 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(2 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_3:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 2] == 0:
					a[i, 2] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(3 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(3 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_4:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 3] == 0:
					a[i, 3] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(4 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(4 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_5:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 4] == 0:
					a[i, 4] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(5 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(5 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_6:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 5] == 0:
					a[i, 5] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(6 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(6 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		if event.key == pygame.K_7:
			for i in range(a.shape[0] - 1, -1, -1):
				if a[i, 6] == 0:
					a[i, 6] = player_number
					if player_number == 1:
						pygame.draw.circle(screen, (255, 0, 0), (int(7 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					if player_number == 2:
						pygame.draw.circle(screen, (255, 255, 0), (int(7 * w / 9 + w / 18), int(i * h / 8 + h / 4)), 20)
					break
			return True
		return False
	if event.type == pygame.KEYUP:
		return False

game_over = False
player_number = 1
a = np.zeros((6, 7), dtype = 'int8')

drawBoard()
while not game_over:
	pygame.time.delay(200)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				game_over = True
	bool = getColumn()
	if bool == True:
		player_number = player_number % 2 + 1
	print(a)
	game_over = check_winner()
	pygame.display.update()

winner = player_number = player_number % 2 + 1
print('Player', winner, 'wins!')
