from turtle import Turtle
FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.current_score = 0

    def display_score(self):
        self.clear()
        self.write(f"Score  : {self.current_score}", False,ALIGNMENT , font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False,ALIGNMENT , font=FONT)
