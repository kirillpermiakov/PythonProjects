from world import World

def getInt(prompt, low=float('-inf'), high=float('inf')):
  ans = low-1
  while not low <= ans <= high or ans == float('-inf'):
    try:
      ans = int(input(prompt))
      if ans < low:
        print(f'The value must be at least {low}')
      if ans > high:
        print(f'The value must be at most {high}')
    except ValueError:
      print('Illegal response')
  return ans

def getYesNo(prompt):
  while True:
    response = input(prompt).strip().lower()
    if response in ('y','yes'):
      return True
    elif response in ('n','no'):
      return False
    else:
      print('Unrecognized response')

def addObstacle(w,rows,cols):
  while True:
    r = getInt('In what row is the obstacle? ', 0, rows-1)
    c = getInt('In what column is the obstacle? ', 0, cols-1)
    if (r,c) == (0,0):
      print('The person starts at (0,0) so that cannot be an obstacle')
    else:
      w.addObstacle(r,c)
      return

# Text based visualizer
class TextViz:

  def __init__(self, world):
    self._w = world

  def update(self):
    rows = w.numRows()
    cols = w.numColumns()
    obstacles = set()
    try:
      obstacles = set(w.getObstacles())
    except:
      pass

    for r in range(rows,-2,-1):
      for c in range(-1,1+cols):
        if 0 <= r < rows and 0 <= c < cols:
          if (r,c) == tuple(w.playerLocation()):
            symbol = 'P'
          elif (r,c) in obstacles:
            symbol = '#'
          else:
            symbol = '.'
        else:
          symbol = '#'  # wall
        print(symbol,end='')
      print()  # end of row
    
               

# cs1graphics based visualizer
class GraphicsViz:
  def __init__(self, world):
    self._w = world
   
    canvas = Canvas(self._w.numColumns()*50, self._w.numRows()*50)

    # Grid graphics
    canvas.setAutoRefresh(False)
    for x in range(self._w.numColumns()):
      for y in range(self._w.numRows()):
        gridSquare = Rectangle(50,50)
        canvas.add(gridSquare)
        gridSquare.moveTo(x*50+25, y*50+25)
        gridSquare.setFillColor("white")
        gridSquare.setBorderColor("black")
    canvas.setAutoRefresh(True)

    # Person graphics
    personLocation = self._w.playerLocation()
    person = Layer()
    
    self._face = Circle(15, Point(personLocation[1]*50+25, self._w.numRows()*50 - personLocation[0]*50 - 25))
    self._face.setFillColor("white")
    self._face.setBorderColor("black")
    self._face.setDepth(2)
    person.add(self._face)

    self._eye1 = Circle(2, Point(personLocation[1]*50+20, self._w.numRows()*50 - personLocation[0]*50-25))
    self._eye1.setFillColor("black")
    self._eye1.setDepth(1)
    person.add(self._eye1)

    self._eye2 = Circle(2, Point(personLocation[1]*50+30, self._w.numRows()*50 - personLocation[0]*50-25))
    self._eye2.setFillColor("black")
    self._eye2.setDepth(1)
    person.add(self._eye2)

    canvas.add(person)
    person.setDepth(1)

    # Obstacle graphics
    obstacles = set()
    try:
      obstacles = set(w.getObstacles())
    except:
      pass

    for obstacle in obstacles:
      obj = Square(50, Point(obstacle[1]*50+25, self._w.numRows()*50 - obstacle[0]*50 - 25))
      obj.setFillColor("black")
      obj.setDepth(2)
      canvas.add(obj)

  def update(self):
    self._face.moveTo(self._w.playerLocation()[1]*50+25, self._w.numRows()*50 - self._w.playerLocation()[0]*50 - 25)
    self._eye1.moveTo(self._w.playerLocation()[1]*50+20, self._w.numRows()*50 - self._w.playerLocation()[0]*50-30)
    self._eye2.moveTo(self._w.playerLocation()[1]*50+30, self._w.numRows()*50 - self._w.playerLocation()[0]*50-30)
 
# setup basic world
print("Welcome to our game. Let's begin by setting up the world.")
rows = getInt('How many rows does the world have? ', 1, float('inf'))
cols = getInt('How many columns does the world have? ', 1, float('inf'))
w = World(rows,cols)

# consider extra credit
moreObstacles = True
firstObstacle = True
while moreObstacles:
  moreObstacles = getYesNo(f"Would you like to add {'an' if firstObstacle else 'another'} obstacle? ")
  if moreObstacles:
    addObstacle(w,rows,cols)
    firstObstacle = False

# consider visualizer
graphics = getYesNo('Would you like a cs1graphics visualization? ')
if graphics:
  from cs1graphics import *
  viz = GraphicsViz(w)
else:
  viz = TextViz(w) 

# start moving
print()
viz.update()
while True:
  raw = input('Enter one of (u)p, (d)own, (l)eft, (r)ight, (m)ove to, (q)uit: ').strip()
  response = raw.upper()[:1]
  if response in ('U','D','L','R','M'):
    if response == 'U':
      success = w.moveUp()
    elif response == 'D':
      success = w.moveDown()
    elif response == 'L':
      success = w.moveLeft()
    elif response == 'R':
      success = w.moveRight()
    else:
      r = getInt('To what row? ')
      c = getInt('To what column? ')
      success = w.moveTo(r,c)

    if not isinstance(success, bool):
      print('WARNING: the method did not return a boolean result')
    else:
      loc = w.playerLocation()
    if not success:
      print('The player was unable to move.')
      print(f'They remain at row {loc[0]}, column {loc[1]}')
    else:
      print(f'The person moved to row {loc[0]}, column {loc[1]}')

    viz.update()

  elif response == 'Q':
    break

  else:
    print('Unrecognized command:',raw)

print('Thanks for playing.')
