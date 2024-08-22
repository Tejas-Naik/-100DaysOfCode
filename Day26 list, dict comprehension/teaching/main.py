a_list = [1, 7, 45, 10]
b_list = []

for i in a_list:
    add_1 = i + 1
    b_list.append(add_1)
    
print(b_list)

new_list = [item + 1 for item in a_list]
print(new_list)
copy_list = [item for item in a_list]
print(copy_list)