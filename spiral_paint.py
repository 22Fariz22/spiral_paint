from PIL import Image, ImageDraw
import numpy as np
import turtle
from math import *

filename = 'image.png'
image = Image.open(filename)  
draw = ImageDraw.Draw(image) 
width = image.size[0]  
height = image.size[1]  
pix = image.load()  

tab_grad = np.zeros((width*2,height*2))
for x in range(width):
    for y in range(height):
       r = pix[x, y][0] 
       g = pix[x, y][1] 
       b = pix[x, y][2] 
       sr = (r + g + b) // 3 
       
       if sr < 40:
           sr = 1
           tab_grad[x,y] = sr
       elif sr < 80:
           sr = 40
           tab_grad[x, y] = sr
       elif sr < 120:
           sr = 80
           tab_grad[x, y] = sr
       elif sr < 160:
           sr = 120
           tab_grad[x, y] = sr
       elif sr < 200:
           sr = 160
           tab_grad[x, y] = sr
       else:
           sr = 200
           tab_grad[x, y] = sr
       draw.point((x, y), (sr, sr, sr)) 
image.save("result.png", "PNG") 


playground = turtle.Screen()       
playground.bgcolor("white")
playground.screensize(width+100, height+100)
playground.title("into Spiral")
t = turtle.Turtle()
t.speed('fastest')
#even in fast mode the turtle is slow, I use this method to show the result instantly.
turtle.tracer(0, 0) 

for i in range(height*5):
    t.pendown()
    x_in_turt = 0
    y_in_turt = 0
    x_in_turt+=int(t.xcor())
    y_in_turt+=int(t.ycor())
    turt_x_coord_in_pil = x_in_turt + int(width / 2)
    turt_y_coord_in_pil = y_in_turt + int(height / 2)
    tg = tab_grad[turt_x_coord_in_pil,turt_y_coord_in_pil]
    
    #If you want a black and white image, use black instead of colors.
    if tg == 1.0:
        t.pen(pencolor= "black", pensize=6, ) 
    elif tg == 40.0:
        t.pen(pencolor= "blue", pensize=5, )   
    elif tg == 80.0:
        t.pen(pencolor= "green", pensize=4) 
    elif tg == 120.0:
        t.pen(pencolor= "purple", pensize=3) 
    elif tg == 160.0:
        t.pen(pencolor= "orange", pensize=2) 
    else:
        t.pen(pencolor= "red", pensize=1)

    """
    Archimedes 'formulas (Archimedes' spiral) in row
    for i in range(200):
    t = i / 20 * pi
    x = (1 + 5 * t) * cos(t)
    y = (1 + 5 * t) * sin(t)
    goto(x, y)
    """
    
    txy = i / 40 * pi
    x = (1 + 1 * txy) * cos(txy)
    y = (1 + 1 * txy) * sin(txy)
    t.goto(x, y)
    t.penup()
    
turtle.update()
turtle.getscreen().getcanvas().postscript(file='outputname.eps')



playground.exitonclick()

