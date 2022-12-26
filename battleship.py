##battleship game##
#window
#Draw grid and coordinates
#Scorebox
#Place ships
##prompt for each ship
#Mirror coordinates
#Opponents?
import pygame
import random

pygame.init()
class ship:
	def __init__(self, length):
		
		self.length = length

CV = ship(5)
BB = ship(4)
DD = ship(3)
SS = ship(3)
PT = ship(2)
##grid variables##
width = 1310
height = 655
gwidth = 40
gheight = 40
mar = 5

gcol = (255, 255, 255)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Battleship Game")
color = (0,0,0)
window.fill(color)

bsc = (255, 0, 0)
row = (13)
col = (13)
##create array##
grid = [[0 for i in range(col)] for r in range(row)]

running = True
#Screen loop#
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
			##clickable##
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			col = pos[0] // (gwidth+mar)
			row = pos[1] // (gheight+mar)
			grid[col][row] = 1
		
        ##Create grid##
	for col in range(13):
		for row in range(13):
			color = gcol
			if grid [col] [row] == 1:
				color = bsc
			pygame.draw.rect(window, color, pygame.Rect(col*(mar+gwidth)+mar,(row*(mar+gheight))+mar,gwidth,gheight))
			pygame.display.flip()



