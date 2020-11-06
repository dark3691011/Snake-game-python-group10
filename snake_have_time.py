"""Snake, classic arcade game.

Excercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import time

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = 10
wall = []
start_time = time.time()
limit_time = 20

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -190 < head.x < 190 and -190 < head.y < 190

def getWall(head):
    return head in wall

def createWall():
    "create wall"
    for y in range(-10,10) :
        wall.append(vector(-100,y*10))
    for y in range(-10,10) :
        wall.append(vector(100,y*10))
    for x in range(-4,5) :
        wall.append(vector(x*10,100))

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    end_time = time.time()
    duration = end_time - start_time
    print(int(duration))

    if not inside(head) :       
        if(-190 > head.x or head.x > 190) :
            head.x = -head.x
        if(-190 > head.y or head.y > 190) :
            head.y = -head.y
        update()

    if head in snake or getWall(head):
        square(head.x, head.y, 9, 'red')
        print(int(duration))
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    "displey wall with 0.9 px solid"
    for body in wall:
        square(body.x, body.y, 9, 'black')

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)
    
        
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(speed, 0), 'Right')
onkey(lambda: change(-speed, 0), 'Left')
onkey(lambda: change(0, speed), 'Up')
onkey(lambda: change(0, -speed), 'Down')
createWall()
print(start_time)
move()
done()