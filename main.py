# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Violetred1")
# timmy.forward(100)
# timmy.goto(29.8, 67.7)
# timmy.pendown()
# timmy.pensize(100)
# timmy.pencolor("brown")
# timmy.fillcolor("violet")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Butterfree"])
table.add_column("Type", ["Electric", "Aqua", "Flyer"])
table.align = "l"
table.valign = "b"
print(table)