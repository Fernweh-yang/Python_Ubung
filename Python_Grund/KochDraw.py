#KochDraw.py
import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main(level):
    turtle.speed(0)
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
level=eval(input("请输入雪花阶数（如1，2，3，4....）"))
main(level)
