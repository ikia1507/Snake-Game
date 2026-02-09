import turtle as t
POSITION=[(0,0),(-20,0),(-40,0)]
class SNAKE:

    def __init__(self):
        self.body=[]
        self.create_snake()
        self.head=self.body[0]

    def new_body(self,position):
        snake_body = t.Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.setposition(position)
        self.body.append(snake_body)

    def create_snake(self):
        for p in POSITION:
            self.new_body(p)

    def extend_body(self):
        self.new_body(self.body[-1].position())

    def snake_move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].setposition(new_x, new_y)
        self.body[0].forward(20)

    def up(self):
       """ for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].setposition(new_x, new_y)
        self.body[0].seth(90)
        self.body[0].forward(20)
        THIS IS NOT NEEDED AS SNAKE IS CONTN MOVING FROM MAIN.PY AND
        HERE IT IS JUST LISTENING TO KEY BOARD SO JUST CHANGE DIRECTION
        AND IT WILL MOVE AS IT IS
        head=body[0] for convenience
        """
       if self.head.heading()==270:
           pass
       else:
           self.body[0].seth(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.body[0].seth(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.body[0].seth(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.body[0].seth(0)



