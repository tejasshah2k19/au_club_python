users = [] # to store multiple users

users.append({'firstName':'ram','contactNum':'123456'})
users.append({'firstName':'ramayan','contactNum':'123423'})
users.append({'firstName':'Ramesh','contactNum':'1234444'})
users.append({'firstName':'sita','contactNum':'123888'})
users.append({'firstName':'laxman','contactNum':'663888'})


while True:
    print("1) Add Contact num\n2) search contact by name\n3) delete by name\n4) view all contacts\n5) search  by number")
    print("6) For Exit")
    # choice = int(input("enter your choice"))
    choice = 4
    if choice == 1:
        isUniq=True

        while isUniq:
            firstName = input("Enter first Name")
            isUniq = False
            for u in users:
                if u.get("firstName") == firstName:
                    print("Please Add name with some unique value")
                    isUniq = True

        contactNum  = input("Enter contact number")
        user ={'firstName':firstName,'contactNum':contactNum}
        users.append(user)
        print("Contact successfully saved")

    elif choice == 2:
        print("Enter Name For Search:")
        name = input()
        for u in users:
            if(u.get('firstName').upper().startswith(name.upper())):
                print(u.get('firstName'), "   ", u.get('contactNum'))

    elif choice ==3:
        print("Enter Name For Delete:")
        name = input()
        for u in users:
            if (u.get('firstName').upper() ==  name.upper()):
                print(u.get('firstName'), " with  ", u.get('contactNum')," is deleted")
                users.remove(u)

    elif choice ==4:
        print("All Contacts")
        print("FIRSTNAME    CONTACT_NUM   FIRSTNAME")
        for u in users:
            print("%-10s   %-11s   %-10s"%(u.get('firstName'),u.get('contactNum'),u.get("firstName")))
        break
    elif choice == 5:
        print("Enter Contact For Search:")
        contactNum = input()
        for u in users:
            if (u.get('contactNum').upper().startswith(contactNum.upper())):
                print(u.get('firstName'), "   ", u.get('contactNum'))

    elif choice == 6:
        exit(0)





