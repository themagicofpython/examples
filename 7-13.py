from time import sleep
import os

maze=[
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,7,1,0,1],
[1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1],
[1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],
[1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def print_maze():
	for r in range(len(maze)):
		s = ''
		for c in range(len(maze[r])):
			if maze[r][c] == 1:
				s += '#'
			elif maze[r][c] == 0:
				s += ' '
			elif maze[r][c] == 3:
				s += '.'
			elif maze[r][c] == 5:
				s += 'X'
			elif maze[r][c] == 7:
				s += 'P'
		print(s)
				
def go(x,y):
	os.system('clear')
	print_maze()
	sleep(0.05)
	if maze[x][y] == 7:
		print("FOUND")
		sleep(2)
	else:
		maze[x][y] = 3
		if maze[x + 1][y] == 0 or maze[x + 1][y] == 7:
			go(x + 1,y)
		if maze[x - 1][y] == 0 or maze[x - 1][y] == 7:
			go(x - 1, y)
		if maze[x][y + 1]==0 or maze[x][y + 1] == 7:
			go(x,y + 1)
		if maze[x][y - 1] == 0 or maze[x][y - 1] == 7:
			go(x, y - 1)
		maze[x][y] = 5		
print("start")
go(1,1)
