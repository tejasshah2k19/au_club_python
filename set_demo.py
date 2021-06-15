x = {1,2,3,4,5,4,5}
print(x)


x = {1,2,3,4,5,6,7}
y = {2,4,6,8}

print(x.intersection(y))
print(x.union(y))

print(x-y)
print(y-x)
print(x.difference(y))
print(y.difference(x))

print(x)
print(y)

#x.intersection_update(y)
#print(x)

x.issuperset(y)
y.issubset(x)

#x.update(y) #x = x.union(y)
#x.remove()  #x.discard()






