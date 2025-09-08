import turtle
import random
turtle.colormode(255)

t = turtle.Turtle()
t.penup()
t.goto(-300, -200)
t.speed('fastest')

def func():
    r,g,b  = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    t.color((r,g,b))
    t.dot(20)
    t.forward(50)

for i in range(1,101):
        func()
        
        if i % 10 == 0:
            t.goto(-300,-200 + (i*4))

screen = turtle.Screen()
screen.exitonclick()



