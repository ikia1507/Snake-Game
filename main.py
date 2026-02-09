import turtle as t
#import random as rd
import time as tm
from food import Food
from Snake import SNAKE
is_game_on=True
#screen setup
screen=t.Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=500,canvheight=500)
screen.tracer(0)
#snake1=t.Turtle(shape="square")
#snake1.color("white")
#snake2=t.Turtle(shape="square")
#snake2.color("white")
#snake2.setpos(x=-20,y=0)
#snake3=t.Turtle(shape="square")
#snake3.color("white")
#snake3.setpos(x=-40,y=0)

#SANKE'S BODY PART

#movement functions for interaction with keyboard
snake=SNAKE()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


"""
for i in range(3):
    snake_body=t.Turtle(shape="square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.setposition(x=X,y=Y)
    X=X-20
    body.append(snake_body)
"""
# SCORE BOARD CODE START
score=0
roxy=t.Turtle()
roxy.setposition(x=0,y=300)
roxy.penup()
roxy.hideturtle()
roxy.color("white")
roxy.write(f"SCORE : {score} ",align="center",font=("interdisplay",10,"bold"))
# SCORE BOARD CODE END
while is_game_on:
    screen.update()
    tm.sleep(0.2)
    snake.snake_move()
    if snake.head.distance(food)<15:
        snake.extend_body()
        food.refresh_food()
        #SCORE BOARD
        score=score+1
        roxy.clear()
        roxy.write(f"SCORE : {score} ", align="center", font=("interdisplay", 10, "bold"))
    # COLLISION
    if snake.head.xcor()>360 or snake.head.xcor()<-360 or snake.head.ycor()>340 or snake.head.ycor()<-340:
         is_game_on=False
         roxy.teleport(0,0)
         roxy.write("GAME OVER !", align="center", font=("interdisplay", 20, "bold"))
    #COLLISION WITH BODY
    for part in snake.body[1:]:
        if snake.head.distance(part)<10:
            is_game_on = False
            roxy.teleport(0, 0)
            roxy.write("GAME OVER !", align="center", font=("interdisplay", 20, "bold"))
"""
    for i in range(len(body)-1,0,-1):
        new_x=body[i-1].xcor()
        new_y = body[i - 1].ycor()
        body[i].setposition(new_x,new_y)
"""
   #Y=rd.randint(-245, 245)
   #food.teleport(x=X,y=Y)
screen.exitonclick()