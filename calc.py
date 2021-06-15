"""

this is known as multi-line comment
"""

'''
this is known as multi-line comment

'''

# -> single line comment

while True:
    a = int(input("Enter num"))
    b = int(input("Enter num"))

    print("1 For Add\n2 For Sub\n3 For Mul\n4 For Exit")
    print("Enter your choice")

    choice = int(input())

    if(choice == 1):
        c=a+b
        print("Addition = ",c)

    elif choice == 2:
        c = a-b
        print("subtraction = ",c)

    elif choice == 3:
        c = a*b
        print("Mul = ",c)

    elif choice == 4:
        print("Thank you")
        #exit(0)
        break
    else:
        print("Invalid choice")
