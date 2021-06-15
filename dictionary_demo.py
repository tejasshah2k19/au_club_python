"""
    dictionary ==>
        we can create using { }
        data cab be store via key value pair
        key => unique , value => can be duplicate



"""


user = { "firstName":"admin","email":"admin@gmail.com","password":"admin123"}
print(type(user))

print(user.get("firstName"))
print(user["firstName"]) #named index

print(user.get("lastName"))
# print(user["lastName"]) #named index
print(user)
user.update({"city":"ahmedabad"})
print(user)
print(len(user))

user.update({"city":"baroda"})
print(user)


user.pop("city")
print(user)
# user.clear()

x = user.popitem()
print(x , " removed")
print(user)

print(user.keys())
print(user.values())

