import keyboard
import turtle
import time

build = turtle.Pen()
build.hideturtle()
build.speed(0)


def block_draw():
    build.pendown()
    build.begin_fill()
    for cube in range(4):
        build.forward(20)
        build.right(90)
    build.end_fill()

    build.forward(20)
    build.penup()


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
        if keyboard.is_pressed('d'):
            if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() + 20), player.ycor())
                time.sleep(0.2)
            watching = 'd'

        # Moving left
        if keyboard.is_pressed('a'):
            if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() - 20), player.ycor())
                time.sleep(0.2)
            watching = 'a'

        if keyboard.is_pressed('w'):
            watching = 'w'

        if keyboard.is_pressed('s'):
            watching = 's'

        # Delete block
        if keyboard.is_pressed('delete'):
            if watching == 'w':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

            if watching == 'a':
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

            if watching == 's':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

            if watching == 'd':
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

            build.color('#3776AB')
            block_draw()

        # Build
        if keyboard.is_pressed('enter'):
            if watching == 'w' and f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

            if watching == 'a' and f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

            if watching == 's' and f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

            if watching == 'd' and f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

            build.color('SaddleBrown')
            block_draw()

        # Jumping
        if keyboard.is_pressed('space') and not jumped:
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




