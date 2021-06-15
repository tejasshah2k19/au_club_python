list = [ 1,2,3,4,"royal",True,55.55]

#any type of data
#mutable
#index

print(list)
print(list[0])
print(list[-1])
print(list[-2])
list[0]=1000
print(list)
print(list[0:3]) # 0 1 2
print(list[0:5:2])
print("original list",list[::])
print(list[::2])
print(list[::-1])
print(list[-3:-1])
print(list[-3:])
print(list[-1:])
print("original list",list[::])
print(list[-3:])


list = [1,2,3,"royal"]

if 11 not in list:
    print("TRUE")
else:
    print("FALSE")


list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    print(i)

i=0
while i< len(list):
    print(list[i])
    i+=1






