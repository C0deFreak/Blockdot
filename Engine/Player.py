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
    jumped = False
    while True:
        # Restart Jump
        if f'({int(xcor())}.00,{int(ycor() - 20)}.00)' in position_list:
            jumped = False

        # Gravity
        if f'({int(xcor())}.00,{int(ycor() - 20)}.00)' not in position_list:
            time.sleep(0.2)
            goto(xcor(), ycor() - 20)
            jumped = True

        # Moving right
        if keyboard.is_pressed('d') and (f'({int(xcor() + 20)}.00,{int(ycor())}.00)' not in position_list):
            goto((xcor() + 20), ycor())
            time.sleep(0.2)

        # Moving left
        if keyboard.is_pressed('a') and (f'({int(xcor() - 20)}.00,{int(ycor())}.00)' not in position_list):
            goto((xcor() - 20), ycor())
            time.sleep(0.2)

        # Jumping
        if keyboard.is_pressed('space') and not jumped:
            high = 0
            time.sleep(0.1)
            if f'({int(xcor())}.00,{int(ycor() + 20)}.00)' in position_list:
                high = 0
            elif f'({int(xcor())}.00,{int(ycor() + 40)}.00)' in position_list:
                high = 1
            else:
                high = 2

            for jump in range(high):
                time.sleep(0.2)
                goto(xcor(), ycor() + 20)

            jumped = True
