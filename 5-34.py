import random

def init_maze(l,w):
  maze = [[1] * l for i in range(w)]
  for i in range(1,w-1,2):
    for j in range(1,l-1,2):
      maze[i][j]=0
  return maze	

def walk(maze, x, y):
  maze[x][y] = 3
  neighbors = [[x - 2, y],[x + 2, y],[x, y - 2],[x, y + 2]]
  random.shuffle(neighbors)
  for newx,newy in neighbors:
    if (newx in range(1,len(maze)) and newy in range(1, len(maze[0]))):
      if maze[newx][newy] == 0: 
        maze[(newx + x) // 2][(newy + y) // 2] = 3 
        walk(maze, newx, newy)

maze = init_maze(20,20)

walk(maze, 1, 1)
print(maze)
