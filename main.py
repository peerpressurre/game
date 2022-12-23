import turtle

#setting up the maze
wn = turtle.screen()
wn.bgcolor('black')
wn.title('A Maze Game')
wn.setup('700,700')

#creating pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('red')
        self.penup()
        self.speed(0)

#creating levels list
levels = ['']

#define first level
level_1 = [

]