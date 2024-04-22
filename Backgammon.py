################################
### kirill.permiakov@slu.edu ###
################################
from cs1graphics import *
size=int(input('Enter the size of one cell: ')) #size of a cell
paper=Canvas(15*size, 13*size, 'burlywood4', 'backgammon') #canvas

#creating line in the middle
line=Path(Point(7.5*size, 0), Point(7.5*size, 13*size))
line.setBorderWidth(size*0.1)
paper.add(line)

#creating rectangles using for loop in left side and then in right side
for r in range(2):
    rect=Rectangle(6*size, 11*size, Point((4*size)+(r*(7*size)), 6.5*size))
    rect.setFillColor('navajowhite')
    paper.add(rect)

#creating triangles at the top and at the bottom but as a layer. I copied it on the right rectangle 
tritotal1=Layer()
for t in range(6):
    tritop=Polygon(Point((1+t)*size, 12*size), Point((2+t)*size, 12*size), Point((1.5+t)*size, 7*size))
    tritop.setFillColor('darkorange3' if t%2==0 else 'tan')
    tritotal1.add(tritop)
    tribottom=tritop.clone()
    tribottom.flip(90)
    tribottom.move(0,-11*size)
    tribottom.setFillColor('tan' if t%2==0 else 'darkorange3')
    tritotal1.add(tribottom)
paper.add(tritotal1)
tritotal2=tritotal1.clone()
tritotal2.move(7*size, 0)
paper.add(tritotal2)
    

#created a for loop in range of numbers and used if statements to move groups of six numbers
for num in range(1,25):
    numbers=Text(str(num), 0.4*size)
    if num<7:
        numbers.moveTo((0.5+num)*size, 12.5*size)
        paper.add(numbers)
    elif num>=7 and num<13:
        numbers.moveTo((1.5+num)*size, 12.5*size)
        paper.add(numbers)
    elif num>=13 and num<19:
        numbers.moveTo(((15-num)+11.5)*size, 0.5*size)
        paper.add(numbers)
    else:
        numbers.moveTo(((7.5-num)+18)*size, 0.5*size)
        paper.add(numbers)


#Used nested for loops here to create my top circles and then the bottom ones
for num,x,whiteOnTop in [(2,1.5,True), (5,6.5,False), (3,9.5,False), (5,13.5,True)]: 
    checkerstop1=Circle((0.9*size)/2, Point(x*size,(1.45*size)))
    checkerstop1.setFillColor('white' if whiteOnTop else 'black')
    paper.add(checkerstop1)
    for n in range(num-1):
        checkerstop2=checkerstop1.clone()
        checkerstop2.move(0,0.9*size+n*0.9*size)
        paper.add(checkerstop2)

    checkersbottom1=Circle((0.9*size)/2, Point(x*size,(1.45*size+10.1*size)))
    checkersbottom1.setFillColor('black' if whiteOnTop else 'white')
    paper.add(checkersbottom1)
    for n in range(num-1):
        checkersbottom2=checkersbottom1.clone()
        checkersbottom2.move(0,-(0.9*size+n*0.9*size))
        paper.add(checkersbottom2)


