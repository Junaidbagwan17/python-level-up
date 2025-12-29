from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon_Name",
                 ["Pickachu", "Squartal", "Charizard"])
#                align="l ")

table.add_column("Type",
                 ["Electric", "Water", "Fire"])
#                 align = "l")

# making table data left aligned
table.align = "l"

print(table)