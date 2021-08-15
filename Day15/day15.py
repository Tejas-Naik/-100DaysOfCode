class Coder():
    def __init__(self, name, programming_language, experience):
        self.name = name
        self.programming_language = programming_language
        self.experience = experience
    
    def give_project(self):
        if self.programming_language == 'python' or self.experience > 2:
            return "Congratulations you got a project!"
    

tejas = Coder('Tejas', 'python', 1.5)
print(tejas.name)
print(tejas.programming_language)
print(tejas.experience)

print(tejas.give_project())