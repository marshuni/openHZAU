import turtle
import math
tt = turtle.Turtle()
sc = tt.getscreen()
sc.setup(600, 600, 100, 100)
sc.bgcolor('yellow')
tt.pencolor(1, 0, 0)
tt.penup()
tt.goto(-200,200)
tt.pendown()
tt.forward(80)
tt.penup()
tt.goto(-200,200)
tt.pendown()
tt.right(90)
tt.forward(160)
tt.penup()
tt.goto(-200,120)
tt.pendown()
tt.left(90)
tt.forward(80)
tt.penup()
tt.goto(-20,200)
tt.pendown()
tt.seth(180) 
tt.circle(80,180)
tt.left(90)
tt.forward(80)
tt.penup()
tt.goto(50,200)
tt.pendown()
tt.right(180)
tt.forward(160)
tt.penup()
tt.goto(50,200)
tt.left(30)
tt.pendown()
tt.forward(320/math.sqrt(3))
tt.left(150)
tt.forward(160)
tt.penup()
tt.goto(180,200)
tt.pendown()
tt.right(180)
tt.forward(160)
tt.penup()
tt.goto(180,200)
tt.pendown()
tt.seth(0)
tt.circle(-40,180)
tt.right(180)
tt.circle(-40,180)
