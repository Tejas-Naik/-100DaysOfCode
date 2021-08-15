# without using List comprehension
numbers = [1, 2, 3]
new_list = []

for num in numbers:
    new_list.append(num * 2)
print(new_list)

# List comprehension
new_list_compre = [num * 2 for num in numbers]
print(new_list_compre)

# List comprehension using range
double_list = [i*2 for i in range(1,5)]
print(double_list)

# conditional List Comprehensions
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# getting names less than 5 letters
short_names = [name for name in names if len(name) < 5]
print(short_names)

capital_names = [name.upper() for name in names if len(name) > 5]
print(capital_names)

