from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.car_set = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            # The car will be created ran bdomly along the y-axis
            random_y = random.randint(-230, 240)
            new_car.goto(300, random_y)
            self.car_set.append(new_car)

    def move(self):
        for car in self.car_set:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT