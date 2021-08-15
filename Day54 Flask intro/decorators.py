import time

def delay_decorator(function):
    def wrapper_function():
        print("-----------------------I am gonna greet you--------------------------")
        time.sleep(2)
        function()
        time.sleep(1)
        print("------------------How do you feel about that greet?-------------------")
        input()
        print("Thank you!")
    return wrapper_function

@delay_decorator
def greet():
    print("Helllllloooooooooo")

greet()

def make_bold(func):
    def wrapper():
        return "<h1>"+func()+"</h1>"
    return wrapper


print("-------------------------------Advanced Decorators---------------------------")

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authenticator_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@authenticator_decorator
def create_blog(user):
    print(f'This is the blogpost of {user.name}')

new_user = User('Tejas')
new_user.is_logged_in = True
create_blog(new_user)