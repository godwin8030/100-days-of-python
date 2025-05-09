from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT) 

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ❌😅.", False, align=ALIGNMENT, font=FONT)
        
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

        
    # def update_score(self):
    #     score = 0
    #     for i in score:
    #         if 