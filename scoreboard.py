from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} high score: {self.high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} high score: {self.high_score}", align=ALIGN, font=FONT)

    def game_end(self):
        self.home()
        self.write(f"GAME END ", align=ALIGN, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode = "w") as data:
                data.write(f"{self.high_score}")


    def reset_score(self):
        self.score = 0
        self.update_score()
        #to know mmore go to 219 video

    def increase_score(self):
        self.score += 1
        self.update_score()

