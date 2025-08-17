from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)

    def refresh_scoreboard(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.write(f"Score = {self.score}", True, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=("Courier", 20, "normal"))

