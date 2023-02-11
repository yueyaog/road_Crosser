from turtle import Screen
import time
from bin.player import Player
from bin.car_manager import CarManager
from bin.scoreboard import Scoreboard
from bin.story import Story
from bin.ending import Ending

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crosser: The Journey Home")
screen.bgcolor("black")
screen.addshape("player_image/squirrel.gif")
screen.tracer(0)

# Begin the game with a background story
story = Story()

user_input = screen.textinput(title="Road Crosser", prompt="Enter X to Find New Place for Me to Survive.")

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = False
if user_input.lower() == 'x':
    story.exit_story()
    game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.car_set:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()
            user_ending_choice = screen.textinput(title="Road Crosser", prompt="Do You Want to Know My Ending (Y/N)? ")
            screen.clear()

            ending = Ending(user_ending_choice, score_board.level)

        if player.ycor() > 280:
            player.restart()
            score_board.level_up()
            car_manager.level_up()




screen.exitonclick()

