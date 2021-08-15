# Reading

# first way
# file = open('myfile.txt')
# contents = file.read()
# print(contents)
# file.close()        # you must close it

# you have not to worry about closing the file
# with open('myfile.txt') as f:
#     contents = f.read()
#     print(contents)

# Writing

# methods in writing/reading files
    # mode="r"  READ(default)
    # mode="w"  WRITE
    # mode="a"  APPEND(add)

# with open('myfile.txt', 'a') as f:
#     contents = f.write("\nHello")

print("*" * 40)

with open('C:/Users/rntej/OneDrive/Desktop/myfile.txt', 'r') as f:
    print(f.read())
# C:\Users\rntej\OneDrive\Desktop
