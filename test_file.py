import turtle

class Seven_seg:
    def __init__(self, my_turtle, color):
        self.turtle = my_turtle
        self.color = color
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setheading(0)
        self.turtle.goto(0, 0)
        self.turtle.pensize(10)

    @staticmethod
    def draw(self, digit):
        if digit == 0:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.penup()

        if digit == 1:
            self.turtle.goto(50, 100)
            self.turtle.pendown()
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.penup()

        if digit == 2:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            for i in range(2):
                self.turtle.forward(100)
                self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.penup()

        if digit == 3:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.forward(-100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.left(90)
            self.turtle.penup()

        if digit == 4:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.forward(-100)
            self.turtle.forward(-100)
            self.turtle.right(90)
            self.turtle.penup()

        if digit == 5:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            self.turtle.forward(100)
            self.turtle.forward(-100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.left(90)
            self.turtle.penup()

        if digit == 6:
            Seven_seg.draw(self, 5)
            self.turtle.goto(-50, 0)
            self.turtle.pendown()
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.penup()
        
        if digit == 7:
            self.turtle.goto(-50, 100)
            self.turtle.pendown()
            self.turtle.forward(100)
            self.turtle.forward(-100)
            Seven_seg.draw(self, 1)

        if digit == 8:
            Seven_seg.draw(self, 0)
            self.turtle.goto(-50, 0)
            self.turtle.pendown()
            self.turtle.forward(100)
            self.turtle.penup()

        if digit == 9:
            Seven_seg.draw(self, 5)
            self.turtle.goto(50, 100)
            self.turtle.pendown()
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.left(90)
            self.turtle.penup()

def clear(my_turtle):
    my_turtle.clear()

def my_delay(dt):
    import time
    start =  time.time()
    while time.time() - start < dt:
        pass

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
a = Seven_seg(Tom, tom_color)
delay_in_seconds = 0.2
while True:
    for i in range(0, 10):
        clear(Tom)
        Seven_seg.draw(Tom, digit = i)
        my_delay(delay_in_seconds)
        turtle.update()

turtle.done()

