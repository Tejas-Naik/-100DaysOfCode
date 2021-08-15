# Type hints are the thing that tell the Python that this is of the type (type())
age: int

age = 15
# if were to pass the other type of data to this it will give you an error

def can_drive(age: int) -> str:
    if age > 18:
        return "You Can Drive"
    else:
        return "YOu can't drive"


print(can_drive(19))
