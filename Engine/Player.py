import keyboard
from turtle import *
import time


def control(position_list):
    penup()
    goto(-515, 195)
    speed(0)
    shapesize(1)
    shape('square')
    color('red')
    showturtle()
    while True:
        if keyboard.is_pressed('d') and (f'({xcor() + 21}0,{round(ycor(), 0)}0)' not in position_list):
            setheading(0)
            forward(21)
            time.sleep(0.2)

        if keyboard.is_pressed('a') and (f'({xcor() - 21}0,{round(ycor(), 0)}0)' not in position_list):
            setheading(180)
            forward(21)
            time.sleep(0.2)

        if keyboard.is_pressed('space'):
            setheading(90)
            for jump in range(14):
                forward(3)
