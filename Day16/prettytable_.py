from prettytable import PrettyTable
import names

print(names.get_full_name())


table = PrettyTable()
table.add_column("Course Names", ['Python for Everybody', '#100DaysOfCode #Python', 'Python developer bootcamp 2021', 'Complete web Developer bootcamp 2021'])
table.add_column("Course website", ['coursera.org', 'udemy.com', 'udemy.com', 'udemy.com'])

print(table)

pokemon_table = PrettyTable()
pokemon_table.add_column('Pokemon Name', ['Pikachu', "Squirtle", 'Charmander'])
pokemon_table.add_column('Pokemon Type', ['Electric', "Water", 'Fire'])
# print(pokemon_table)

first_names = PrettyTable()
first_names.add_column("First Name", [names.get_first_name() for _ in range(10)])
first_names.add_column("Last Name", [names.get_last_name() for _ in range(10)])
first_names.align = 'l'
print(first_names)
