import keyboard
from turtle import *
import time


def control(position_list):
    penup()
    goto(-10, 210)
    speed(0)
    shapesize(1)
    shape('square')
    color('red')
    showturtle()
    while True:
        # Gravity
        if f'({int(xcor())}.00,{int(ycor() - 20)}.00)' not in position_list:
            time.sleep(0.2)
            goto(xcor(), ycor() - 20)

        # Moving right
        if keyboard.is_pressed('d') and (f'({int(xcor() + 20)}.00,{int(ycor())}.00)' not in position_list):
            goto((xcor() + 20), ycor())
            time.sleep(0.2)

        # Moving left
        if keyboard.is_pressed('a') and (f'({int(xcor() - 20)}.00,{int(ycor())}.00)' not in position_list):
            goto((xcor() - 20), ycor())
            time.sleep(0.2)

        # Jumping
        if keyboard.is_pressed('space'):
            time.sleep(0.1)
            #if keyboard.is_pressed('d') and (f'({int(xcor() + 21)}.00,{int(ycor() + 21)}.00)' not in position_list):
             #   for jump in range(14):
              #      setheading(90)
               #     forward(3)
                #goto((xcor() + 21), ycor())
            #elif keyboard.is_pressed('a') and (f'({int(xcor() - 21)}.00,{int(ycor())}.00)' not in position_list):
             #   for jump in range(7):
              #      setheading(90)
               #     forward(3)
                #goto((xcor() - 21), ycor())
            #else:
            for jump in range(2):
                time.sleep(0.2)
                goto(xcor(), ycor() + 20)
