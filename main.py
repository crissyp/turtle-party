# Turtle Party
# By Crissy Pohl
# 7.12.24

import turtle

turtle.color("violet red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
 
def polygon(sides, len):
  for i in range(sides):
    turtle.forward(len)
    turtle.left(360 / sides)
 
polygon(4, 100)
back(125)
polygon(3, 50)
