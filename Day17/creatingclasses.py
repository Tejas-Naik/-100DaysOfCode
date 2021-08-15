class User:
    def __init__(self, name, id):      # Initializing an attribute name and id
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0

    def celebrity_mode(self):
        # when you are calling a method you can change the attribute of tha class or add another one
        # here we are modifying the value of followers attribute
        self.followers = 100000

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Tejas", "001")


print(user1.name)
print(user1.id)
print(user1.followers)

user1.celebrity_mode()
print("Celebrity", user1.followers)

user2 = User("RN", '007')


print("********************************************************8")
user1.follow(user2)

print(user2.followers)
