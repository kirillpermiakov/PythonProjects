from cs1graphics import *

paper=Canvas(1000,600, 'skyBlue', 'Bear and Lion')

whitegrass=Rectangle(1000,200, Point(500,500))
whitegrass.setFillColor(240,248,255)
paper.add(whitegrass)

bear=Layer()
bearhead=Circle(100, Point(300,400))
bearbody=Ellipse(200,400, Point(300,500))
#beararm1=Ellipse(50,200, Point(200,

