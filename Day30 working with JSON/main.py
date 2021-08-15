# Catching Exceotions
try:
    pass    # something that can cause a Exception

except:
    pass    # Do this if there is an exception

else:
    pass    # If there is were no exception in your code (Passed: Try and Except block)

finally:
    pass    # Do this no matter what happened above just do it!


# try:
#     file = open('a_file.txt')
# except:
#     # print("There is no such file")
#     file = open('a_file.txt', 'w')  # if you open a file in a write mode it will create a file

# if you have two errors in same try block its better to use two different Except blocks 
try:
    file = open('a_file.txt')
    dictionary = {"key": "Value"}
    print(dictionary['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write("Finally I got created! hurray")
except KeyError as error_message:
    print(f"The key {error_message} does not exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed!")



# Raising our own Exceptions:
print()
height = 2.3 # float(input("Please enter your height in meters: "))
weight = 45  # float(input("Please enter your weight in 'kg': "))

if height > 3:
    raise ValueError("Humans height could not be over 3 meters")

bmi = weight / height**2
print(bmi)

print()
print()
print()
print()
print()
print()


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes = total_likes + 0
        pass

print(total_likes)



# JSON = JavaScript Object Notation
