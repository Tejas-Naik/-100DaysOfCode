class User:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def attendence(self):
        """
            This function takes ID of an employee and adds him to attendees list
        """
        attendence = []
        attendence.append(self.name)
        attendence.append(self.id)
        return attendence

tejas = User(1, 'Tejas')
print(tejas.attendence())
rn_tejas = User(7, 'RN Tejas')
print(rn_tejas.attendence())
