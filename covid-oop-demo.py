import random
class Patient:

    def __init__(self):
        self.name = ""
        self.tokeNum = 0
        self.tokenType = "" # t | d


    def input(self):
        print("Enter your name")
        self.name = input()
        print("do you want RTPCR?y|n?")
        rtpcr = input()
        if rtpcr.lower() == 'y':
            self.tokenType = "t"
        else:
            self.tokenType = "d"
        self.tokeNum  =  int( random.random()* 100000)
    def display(self):
        print(self.name,"     ",self.tokeNum,"     ",self.tokenType)





#logic
patients = []

while True :
    print("1 For Registration\n2 For Display\n3 For Exit")
    choice = int(input())

    if choice == 1:
         p = Patient()
         p.input()
         patients.append(p)
    elif choice == 2:
        for p in patients:
            p.display()
    elif choice == 3:
        print("good bye")
        break


