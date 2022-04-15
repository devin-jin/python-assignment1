import turtle,random
def drawdot():
    turtle.right(90)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.forward(1)
    turtle.right(180)
    turtle.penup()
    turtle.fd(50)
    turtle.right(90)
    turtle.fd(20)
def drawgap():
    turtle.penup()
    turtle.fd(6)
def drawline(draw):
    drawgap()
    turtle.pendown()  if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawrandom():
    a=str(round(random.uniform(0,10),2))
    for i in a:
        drawdigit(eval(i)) if '0'<=i<='9' else drawdot()
def main():
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(10)
    drawrandom()
    turtle.hideturtle()
    turtle.done()
main()

