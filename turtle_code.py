from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Scatterbug","Metapod","Bidoof"])
table.add_column("Type", ["Electric","Bug","Bug","Normal"])


print(table)