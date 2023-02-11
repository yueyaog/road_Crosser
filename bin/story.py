from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Story(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Road Crosser: The Journey Home")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.background()



    def background(self):
        self.setpos(-25, -200)
        self.write("""
        Born in tree, as a squirrel. \n
        Mom, sis, bro, no dad known. \n
        Played, ate, chased with siblings. \n
        Home tree gone, bro lost, park too. \n 
        Now, just cars, not happy park. \n
        Memories lost, peaceful days gone.
        """, False, align=ALIGNMENT, font=FONT)

    def exit_story(self):
        self.clear()

