from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Butterfree"])
table.add_column("Type", ["Electric", "Aqua", "Flyer"])
table.align = "l"
table.valign = "b"
print(table)
