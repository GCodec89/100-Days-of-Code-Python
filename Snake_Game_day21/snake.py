from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self, dimension_snake):
        self.body = []
        self.create_snake(dimension_snake)
        self.head = self.body[0]
        self.direction = RIGHT
        self.next_direction = RIGHT 
        
    def create_snake(self, dim):
        i = 0
        while i < dim:
            x = i * -20
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(x, 0)
            self.body.append(snake_body)
            i += 1	
    
    def add_body(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.body.append(snake_body)
    
    def extend(self):
        self.add_body(self.body[-1].position())
        
    
    def move(self):
        for b in range(len(self.body) - 1, 0, -1):
            new_x = self.body[b - 1].xcor()
            new_y = self.body[b - 1].ycor()
            self.body[b].goto(new_x, new_y)
        self.direction = self.next_direction
        self.head.setheading(self.direction)
        self.head.forward(MOVE_DISTANCE)
    
    
    def snake_up(self):
        if self.direction != DOWN:
            self.next_direction = UP
        
    def snake_down(self):
        if self.direction != UP:
            self.next_direction = DOWN
        
    def snake_right(self):
        if self.direction != LEFT:
            self.next_direction = RIGHT
        
    def snake_left(self):
        if self.direction != RIGHT:
            self.next_direction = LEFT