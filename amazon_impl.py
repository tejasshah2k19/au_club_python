users = []
products = [{"productId":1,"name":"tv","price":25000},{"productId":2,"name":"laptop","price":89000},{"productId":3,"name":"iphone","price":75000}]

users.append({"userId":1,"name":"anny","email":"a","password":"a","role":"user"})
users.append({"userId":2,"name":"admin","email":"admin@gmail.com","password":"admin","role":"admin"})

while True:
    print("1 For Sigup\n2 For Login")
    choice = int(input("Enter choice"))
    if choice == 1:
        print("Enter Name email and password")
        userId=1212
        name = input()
        email = input()
        password = input()

        users.append({"userId":userId,"name":name,"email":email,"password":password})

    elif choice==2:
      currentUser = None
      print("Enter email and password for Login")
      email = input()
      password = input()
      for u in users:
          if u.get("email") == email and u.get("password") == password:
                currentUser= u
                # print(currentUser)
                break
      if currentUser == None:
          print("Invalid credentials")
      elif currentUser.get("role") == "admin":
          print("Welcome admin , ",currentUser.get("name"))
      elif currentUser.get("role")=="user":
          user_choice = 0
          while user_choice != 4:
              print("Welcome user , ",currentUser.get("name"))
              print("1 For View Product")
              print("2 For View Cart")
              print("3 For Buy Product")
              print("4 For Logout")
              user_choice = int(input("enter choice"))
              if user_choice == 4:
                  print("...Thank you....")
              if user_choice == 2:
                  print(currentUser.get("cart"))
              if user_choice == 3:
                  print(products)
                  print("Enter product id for purchase")
                  proId = int(input()) #3 2
                  for p in products:
                      if p.get("productId") == proId:
                          cart = currentUser.get("cart")
                          if cart is None:
                              cart = list()
                          isPresent = False
                          for c in cart:
                                  if c.get("productId") == proId:
                                      c.update({"qty":c.get("qty")+1})
                                      isPresent = True
                                      break
                          if isPresent == False:
                              t = p.copy()
                              t.update({"qty":1})
                              cart.append(t)

                          currentUser.update({"cart":cart})
    else:
        print("good bye")
        break