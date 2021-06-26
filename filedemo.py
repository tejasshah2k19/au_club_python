#file

 #w ->write --> if file is not present then it will create new
                                #--> what if file is alread present ? over write data
                                #-> "a" -> append
                                #-> "w" -> write
                                #-> "r" -> read
                                #-> "x" -> create file ,if file is present then throw error
                                #-> "t" -> text [default]
                                #-> "b" -> binary [ images]

'''
f = open("data.txt","w")
f.write("this is the easiest way to write data in file")
f.close()

f = open("number.txt","w")
for i in range(1,6):
    n = input("enter number")
    f.write(n+"\n")
    f.writable()
f.close()

'''


f = open("data.txt","r")

#d = f.read()#->read everyting
# read(4) -> read only 4 characters
#d = f.readline() #read single line
#print(d,end="")
#d = f.readline() #read single line
#print(d)



allLines = f.readlines() # this will returns all the lines with a list
print(allLines)
print(allLines[0])

f.close()

