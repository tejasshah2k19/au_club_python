class Student:
    x=90

    #default constructor
    # def __init__(self):
    #      self.name = ""
    #      self.id = 0
    #      self.city = "ahmedabad"
    #      self.__age = 123

    def __init__(self,name="N",id=0,city="ahd",age=0):
        self.name = name
        self.id=id
        self.city = city
        self.__age = age

    def display(self):
        print(self.name," ",self.id," ",self.city," ",self.__age)


    def add(self):
        x=900
        y=90 # local
        self.z=100 # instance
        print("add => ",x)  #this => self
        print("add => ",self.x)


# s = Student()
# print(s.x)
# s.add()


# s = Student()
# s.display()
# print(s.city)
#print(s.__age)

s = Student("ram",12,"ahd",23)
s.display()

s1 = Student()
s1.display()

s2 = Student(id=12)
s2.display()