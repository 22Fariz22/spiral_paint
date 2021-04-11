# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
import turtle
from math import *

filename = 'image.png'
image = Image.open(filename)  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

tab_grad = np.zeros((width*2,height*2)) # массив градиентов
for x in range(width):
    for y in range(height):
       r = pix[x, y][0] #узнаём значение красного цвета пикселя
       g = pix[x, y][1] #зелёного
       b = pix[x, y][2] #синего
       sr = (r + g + b) // 3 #среднее значение
       # далее 255 градиентов серого сокращаем до 5
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
       draw.point((x, y), (sr, sr, sr)) #рисуем пиксел
       # print(f"x:{x}, y:{y}, grad:{sr}")
image.save("result.png", "PNG") #не забываем сохранить изображение


playground = turtle.Screen()       # use nouns for objects, play is a verb
playground.bgcolor("white")
playground.screensize(width+100, height+100)
playground.title("into Spiral")
t = turtle.Turtle()
t.speed('fastest')
# t.mainloop()
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
    # print(type(tg))
    # print(tg)
    if tg == 1.0:
        t.pen(pencolor= "black", pensize=6, ) #f29130
    elif tg == 40.0:
        t.pen(pencolor= "blue", pensize=5, )  # "#ad8b10"
    elif tg == 80.0:
        t.pen(pencolor= "green", pensize=4)  # "#32f075"
    elif tg == 120.0:
        t.pen(pencolor= "purple", pensize=3)  # "#09dba7"
    elif tg == 160.0:
        t.pen(pencolor= "orange", pensize=2)  # "#1169ed"
    else:
        t.pen(pencolor= "red", pensize=1)

    txy = i / 40 * pi
    x = (1 + 1 * txy) * cos(txy)
    y = (1 + 1 * txy) * sin(txy)
    t.goto(x, y)
    t.penup()
    # print(round(t.xcor(),0),'  ',round(t.ycor(),0))
turtle.update()
turtle.getscreen().getcanvas().postscript(file='outputname.eps')



playground.exitonclick()



"""
colorization image

    if tg == 1.0:
        t.pen(pencolor="#0b0861", pensize=6, )
    elif tg == 40.0:
        t.pen(pencolor="#1169ed", pensize=5, ) # blue
    elif tg == 80.0:
        t.pen(pencolor="#09dba7", pensize=4 ) # green
    elif tg == 120.0:
        t.pen(pencolor="#32f075", pensize=3 ) # green
    elif tg == 160.0:
        t.pen(pencolor="#ad8b10", pensize=2) # purple
    else:
        t.pen(pencolor="#f29130", pensize=1) # red

"""

"""
negativ image

    if tg == 1.0:
        t.pen(pencolor="black", pensize=6, )
    elif tg == 40.0:
        t.pen(pencolor="black", pensize=5, ) # blue
    elif tg == 80.0:
        t.pen(pencolor="black", pensize=4 ) # green
    elif tg == 120.0:
        t.pen(pencolor="black", pensize=3 ) # green
    elif tg == 160.0:
        t.pen(pencolor="black", pensize=2) # purple
    else:
        t.pen(pencolor="black", pensize=1) # red
"""



"""
try replace height and width in array bc of out of index
"""


"""
       if sr < 50:
           sr = 1
           tab_grad[x,y] = sr
       elif sr < 100:
           sr = 100
           tab_grad[x, y] = sr
       elif sr < 150:
           sr = 150
           tab_grad[x, y] = sr
       elif sr < 200:
           sr = 200
           tab_grad[x, y] = sr
       else:
           sr = 250
           tab_grad[x, y] = sr
       draw.point((x, y), (sr, sr, sr)) #рисуем пиксел
       # print(f"x:{x}, y:{y}, grad:{sr}")
image.save("result.png", "PNG") #не забываем сохранить изображение



playground = turtle.Screen()       # use nouns for objects, play is a verb
playground.bgcolor("white")
playground.screensize(width+50, height+50)
playground.title("Dürer")
t = turtle.Turtle()
t.speed('fastest')


for i in range(20000):
    t.pendown()
    x_in_turt = 0
    y_in_turt = 0
    x_in_turt+=int(t.xcor())
    y_in_turt+=int(t.ycor())
    turt_x_coord_in_pil = x_in_turt + int(width / 2)
    turt_y_coord_in_pil = y_in_turt + int(height / 2)
    tg = tab_grad[turt_x_coord_in_pil,turt_y_coord_in_pil]
    # print(type(tg))
    # print(tg)
    if  tg == 1.0:
        t.pensize(1)
    elif tg == 50.0:
        t.pensize(2)
    elif tg == 100.0:
        t.pensize(3)
    elif tg == 150.0:
        t.pensize(4)
    elif tg == 200.0:
        t.pensize(5)
    else:
        t.pensize(6)
    txy = i / 50 * pi
    x = (2 + 0.9 * txy) * cos(txy)
    y = (2 + 0.9 * txy) * sin(txy)

    t.goto(x, y)
    t.penup()
"""