import keyboard
import turtle
import time


def control(position_list):
    player = turtle.Pen()
    player.penup()
    player.goto(-10, 210)
    player.speed(0)
    player.shapesize(1)
    player.shape('square')
    player.color('red')
    player.showturtle()
    jumped = False
    while True:
        # Restart Jump
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
            jumped = False

        # Gravity
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
            time.sleep(0.2)
            player.goto(player.xcor(), player.ycor() - 20)
            jumped = True

        # Moving right
        if keyboard.is_pressed('d') and (f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list):
            player.goto((player.xcor() + 20), player.ycor())
            time.sleep(0.2)

        # Moving left
        if keyboard.is_pressed('a') and (f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list):
            player.goto((player.xcor() - 20), player.ycor())
            time.sleep(0.2)

        # Jumping
        if keyboard.is_pressed('space') and not jumped:
            high = 0
            time.sleep(0.1)
            if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                high = 0
            elif f'({int(player.xcor())}.00,{int(player.ycor() + 40)}.00)' in position_list:
                high = 1
            else:
                high = 2

            for jump in range(high):
                time.sleep(0.2)
                player.goto(player.xcor(), player.ycor() + 20)

            jumped = True




