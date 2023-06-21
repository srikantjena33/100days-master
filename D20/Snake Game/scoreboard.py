from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier",24, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}", align= ALLIGNMENT , font= FONT )
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial",24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        