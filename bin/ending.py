from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Ending(Turtle):

    def __init__(self, user_ending_choice, ending_level):
        super().__init__()
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Road Crosser: The Journey Home")
        self.color("White")
        self.hideturtle()
        self.penup()
        self.input = user_ending_choice
        self.level =  ending_level
        # Based on user input, provide corresponding ending screen
        if self.input.lower() != "y":
            self.ending_dialog()
        elif self.input.lower() == "y" and self.level <= 3:
            self.mount_ending()
        elif self.input.lower() == "y" and 3 < self.level <= 15:
            self.smear_ending()
        elif self.input.lower() == "y" and self.level > 15:
            self.happy_ending()

    def ending_dialog(self):
        self.setpos(-25, -25)
        self.write("""
        Dead on the road, left alone \n
        Car took my life, it's shown \n
        Laying here, all alone \n
        No goodbyes, just gone. \n
        (Click to Exit)        
        """, False, align=ALIGNMENT, font=FONT)

    def mount_ending(self):
        self.setpos(-25, -25)
        self.write("""
        I once climbed tall oak trees \n
        Chased nuts with such ease \n
        Now, I'm mounted with breeze \n
        In a house, where I freeze \n
        Squished by a car, with ease. \n
        (Click to Exit)        
        """, False, align=ALIGNMENT, font=FONT)

    def smear_ending(self):
        self.setpos(-25, -25)
        self.write("""
        I once was full of life, \n
        A car came by, so swift and fleet, \n
        My mom and sister couldn't see, \n
        I'm just a crumb on the street, \n
        Life is short, always be careful, \n
        my friend, don't you see. \n
        (Click to Exit)        
        """, False, align=ALIGNMENT, font=FONT)

    def happy_ending(self):
        self.setpos(-25, -25)
        self.write("""
        My friend, you helped me, \n
        You might lost the game, \n
        But, I am in a new home, \n
        No more bustling cars, \n
        Lots of acorns , \n
        I’m fat, healthy, and happy.\n
        (Click to Exit)        
        """, False, align=ALIGNMENT, font=FONT)