from prettytable import PrettyTable

table = PrettyTable()
table.add_column('pokemon name', ['pikachu','charmander', 'squirtle'])
table.add_column('Type', ['Electric','Fire', 'Water'])

table.align = 'l'

print(table)
