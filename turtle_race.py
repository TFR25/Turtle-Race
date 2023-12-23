from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

race = False

user_bet = screen.textinput(title="Let the betting begin!", prompt="Choose a color of the rainbow: ")

ycor = [-124, -70, -24, 24, 70, 124]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

contestants = []

for i in range(len(colors)):
    new_contestant = Turtle(shape="turtle")
    new_contestant.color(colors[i])
    new_contestant.penup()
    new_contestant.goto(x=-200, y=ycor[i])
    contestants.append(new_contestant)

if user_bet:
    race = True

while race:
    for turtle in contestants:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"Yay, the {winner} turtle won. You win 🥇")
            else:
                print(f"Sorry, the {winner} turtle won. You lose 😭")

        distance = random.randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()
