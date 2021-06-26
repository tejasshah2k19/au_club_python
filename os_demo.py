import os

#os.mkdir("demo")

#
# getPWD = os.getcwd()
# os.rmdir("demo")
# print(getPWD)

#os.mkdir("demo")
os.chdir("demo")
print(os.getcwd())
x = open("new.txt","w")
x.write("demo")
x.close()
# os.rename("oldfilename.txt","newfilename.txt")


