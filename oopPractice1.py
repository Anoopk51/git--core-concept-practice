'''
1.
'''

class Institute:

    def __init__(self,name,stablishYear):
        self.name = name
        self.stablishYear = stablishYear

class Student(Institute):

    def __init__(self,stuName,age,branch,name,stablishYear):
        super().__init__(name,stablishYear)
        self.stuName = stuName
        self.age =  age
        self.branch = branch

obj = Student("Anoop",22,"IT","SCRIET",2003)
print(obj.stuName)
print(obj.age)
print(obj.branch)
print(obj.name)
print(obj.stablishYear)



'''
1.
'''

class Company:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        # pass
        