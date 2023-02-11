from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-240, 260)
        self.level = 1
        self.write(f"Level {self.level}", False, "center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, "center", font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=FONT)

    def congrats(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Congrats!", False, "center", font=FONT)


